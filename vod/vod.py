import logging
from typing import Union

from arvan.api import Arvan
from vod.channel import Channel
from vod.video import Video


class VOD(Arvan):
	get_channels_url = 'https://napi.arvancloud.com/vod/2.0/channels'
	get_videos_urls = 'https://napi.arvancloud.com/vod/2.0/channels/{channel_id}/videos'

	def get_channels(self, query_params: dict = None):
		r = self._send_request('GET', self.get_channels_url, query_params)
		return [Channel(**x) for x in r['data']]

	def get_videos(self, channel: Union[int, Channel]):
		channel_id = channel
		if isinstance(channel, Channel):
			channel_id = channel.channel_id
		r = self._send_request('GET', self.get_videos_urls.format(**{'channel_id': channel_id}))
		return [Video(**x) for x in r['data']]
