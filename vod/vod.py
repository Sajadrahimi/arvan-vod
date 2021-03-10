from typing import Union

import requests

from arvan.api import Arvan
from vod.channel import Channel
from vod.video import Video


class VOD(Arvan):
	get_channels_url = 'https://napi.arvancloud.com/vod/2.0/channels'
	get_videos_urls = 'https://napi.arvancloud.com/vod/2.0/channels/{channel_id}/videos'
	add_video_url = 'https://napi.arvancloud.com/vod/2.0/channels/{channel}/videos'

	def get_channels(self, query_params: dict = None):
		r = self._send_request('GET', self.get_channels_url, query_params)
		return [Channel(**x) for x in r]

	def get_videos(self, channel: Union[int, Channel]):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		r = self._send_request('GET', self.get_videos_urls.format(**{'channel_id': channel_id}))
		return [Video(**x) for x in r]

	def add_video(self, channel: Union[int, Channel], title, video_url,
				  profile_id=None, description=None,
				  thumbnail_time=None, watermark_id=None, watermark_area=None, convert_info=None,
				  convert_mode: str = 'auto',
				  parallel_convert: bool = False):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		url = self.add_video_url.format(**{'channel': channel_id})
		r = self._send_request('post', url, json={
							  "title": title,
							  'description': description,
							  'video_url': video_url,
							  'convert_mode': convert_mode,
							  'parallel_convert': parallel_convert,
						  })
		print(r)
		return Video(**r)
