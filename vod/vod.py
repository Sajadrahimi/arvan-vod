import base64
import os
from typing import Union

import requests

from arvan.api import Arvan
from vod.channel import Channel
from vod.video import Video


class VOD(Arvan):
	get_channels_url = 'https://napi.arvancloud.com/vod/2.0/channels'
	get_videos_urls = 'https://napi.arvancloud.com/vod/2.0/channels/{channel_id}/videos'
	add_video_url = 'https://napi.arvancloud.com/vod/2.0/channels/{channel}/videos'
	request_upload_video_url = 'https://napi.arvancloud.com/vod/2.0/channels/{channel}/files'
	upload_video_url = 'https://napi.arvancloud.com/vod/2.0/channels/{channel}/files/{file}'
	store_new_video_url = 'https://napi.arvancloud.com/vod/2.0/channels/{channel}/videos'
	get_file_url = 'https://napi.arvancloud.com/vod/2.0/files/{file}'
	list_files_url = 'https://napi.arvancloud.com/vod/2.0/channels/{channel}/files'

	def get_channels(self, query_params: dict = None):
		r = self._send_request('GET', self.get_channels_url, query_params)
		return [Channel(**x) for x in r]

	def get_videos(self, channel: Union[int, Channel], title: str = None):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		query_params = {'per_page': 1000}
		if title:
			query_params['filter'] = title
		r = self._send_request('GET', self.get_videos_urls.format(**{'channel_id': channel_id}),
							   query_params=query_params)
		if len(r) == 1:
			return Video(**r[0])
		return [Video(**x) for x in r]

	def add_video(self, channel: Union[int, Channel], title: str = None, video_url: str = None, file_id: str = None,
				  profile_id=None, description=None,
				  thumbnail_time=None, watermark_id=None, watermark_area=None, convert_info=None,
				  convert_mode: str = 'auto',
				  parallel_convert: bool = False):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		if bool(file_id) == bool(video_url):
			raise ValueError('Either file_id or video_url must be provided.')
		if not title and file_id:
			title = self.get_file(file_id).get('filename')
		if file_id:
			source = {'file_id': file_id}
		elif video_url:
			source = {'video_url': video_url}
		base_data = {
			"title": title,
			'description': description,
			'convert_mode': convert_mode,
			'parallel_convert': parallel_convert,
		}
		url = self.add_video_url.format(**{'channel': channel_id})
		r = self._send_request('post', url, json={**base_data, **source})
		try:
			return Video(**r)
		except Exception as e:
			print(e)
			return r

	def request_upload(self, channel: Union[int, Channel], file_path: str, file_type: str = 'video/mp4',
					   tus_resumable: str = "1.0.0", upload_length: int = 10096, upload_metadata: str = None):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		url = self.request_upload_video_url.format(**{'channel': channel_id})
		file_name = os.path.basename(file_path)
		size = os.stat(path=file_path).st_size
		r = self._send_request('post', url,
							   headers={
								   'tus-resumable': tus_resumable,
								   'upload-length': str(size),
								   'upload-metadata': "filetype %s,filename %s" % (
									   base64.b64encode(file_type.encode()).decode('ascii'),
									   base64.b64encode(file_name.encode()).decode('ascii'))
							   },
							   )
		upload_url = r.headers.get('location')
		if not upload_url:
			raise AttributeError
		file_id = upload_url.split('/')[-1]
		requests.patch(upload_url,
					   headers=self._build_headers({'content-type': 'application/offset+octet-stream',
													'upload-offset': '0',
													'tus-resumable': tus_resumable}),
					   data=open(file_path, 'rb'))
		return file_id

	def get_file(self, file_id: str):
		return self.send_request('get', self.get_file_url.format(**{'file': file_id}))

	def list_files(self, channel: Union[str, Channel]):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		return self.send_request('get', self.list_files_url.format(**{'channel': channel_id}))
