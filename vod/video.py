from typing import List

from arvan.types import DynamicType


class FileInfo(DynamicType):
	class General(DynamicType):
		duration: int
		format: str
		bit_rate: int
		size: int

	class Video(DynamicType):
		codec: str
		width: int
		height: int
		frame_rate: str
		bit_rate: str

	class Audio(DynamicType):
		codec: str
		sample_rate: str
		bit_rate: str
		channel_layout: str

	def __init__(self, **kwargs):
		self.general = None
		self.video = None
		self.audio = None
		if 'general' in kwargs:
			self.general = self.General(**kwargs['general'])
			del kwargs['general']
		if 'video' in kwargs:
			self.video = self.Video(**kwargs['video'])
			del kwargs['video']
		if 'audio' in kwargs:
			self.audio = self.Audio(**kwargs['audio'])
			del kwargs['audio']

		super().__init__(**kwargs)


class ConvertInfo(DynamicType):
	audio_bitrate: int
	video_bitrate: int
	resolution: str


class Video(DynamicType):
	video_id: str
	title: str
	description: str
	file_info: FileInfo
	thumbnail_time: int
	status: str
	job_status_url: str
	available: bool
	convert_mode: str
	convert_info: List[ConvertInfo]
	created_at: str
	updated_at: str
	completed_at: str
	parallel_convert: int
	directory_size: str
	config_url: str
	mp4_videos: List[str]
	hls_playlist: str
	dash_playlist: str
	thumbnail_url: str
	tooltip_url: str
	video_url: str
	player_url: str
	# channel: Channel

	def __init__(self, **kwargs):
		# if 'file_info' in kwargs:
		# 	self.file_info = get_type(self, (**kwargs['file_info'])
		# 	del kwargs['file_info']

		if 'convert_info' in kwargs:
			self.convert_info = []
			for convert_info in kwargs['convert_info']:
				self.convert_info.append(ConvertInfo(**convert_info))
			del kwargs['convert_info']

		if 'mp4_videos' in kwargs:
			self.mp4_videos = kwargs['mp4_videos']
			del kwargs['mp4_videos']
		kwargs['video_id'] = kwargs.pop('id')
		del kwargs['channel']
		super().__init__(**kwargs)

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.__str__()