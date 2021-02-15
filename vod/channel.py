class Channel:
	channel_id: str
	title: str
	description: str
	secure_link_enabled: bool
	secure_link_key: str
	secure_link_with_ip: bool
	ads_enabled: bool
	present_type: str
	campaign_id: str

	def __init__(self, channel_id: str = None, title: str = None, description: str = None,
				 secure_link_enabled: str = None,
				 secure_link_key: str = None,
				 secure_link_with_ip: str = None,
				 ads_enabled: str = False,
				 present_type: str = None,
				 campaign_id: str = None, **kwargs):
		self.campaign_id = campaign_id
		self.present_type = present_type
		self.ads_enabled = bool(ads_enabled)
		self.secure_link_with_ip = bool(secure_link_with_ip)
		self.secure_link_key = secure_link_key
		self.secure_link_enabled = bool(secure_link_enabled)
		self.description = description
		self.title = title
		self.channel_id = channel_id
		for k in kwargs:
			if k == 'id':
				setattr(self, 'channel_id', kwargs[k])
			setattr(self, k, kwargs[k])

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.__str__()
