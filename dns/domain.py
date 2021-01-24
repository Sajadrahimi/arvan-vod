from datetime import datetime
from typing import List


class Domain:
	# TODO add domain features
	domain_id: str
	user_id: str
	domain: str
	name: str
	status: str
	smart_routing_status: str
	parent_domain: bool
	is_paused: bool
	ns_keys: List[str]
	current_ns: List[str]
	created_at: datetime
	updated_at: datetime

	def __init__(self, domain_id: str = None, user_id: str = None, domain: str = None, name: str = None,
				 status: str = None,
				 smart_routing_status: str = None,
				 parent_domain: bool = False, is_paused: bool = False, ns_keys: List[str] = None,
				 current_ns: List[str] = None,
				 created_at=None, updated_at=None, **kwargs):
		if isinstance(created_at, str):
			try:
				created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
			except ValueError:
				raise ValueError('created_at must match %Y-%m-%dT%H:%M:%SZ')
		if isinstance(updated_at, str):
			try:
				updated_at = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ')
			except ValueError:
				raise ValueError('updated_at must match %Y-%m-%dT%H:%M:%SZ')

		self.updated_at = updated_at
		self.created_at = created_at
		self.current_ns = current_ns
		self.ns_keys = ns_keys
		self.is_paused = is_paused
		self.parent_domain = parent_domain
		self.smart_routing_status = smart_routing_status
		self.status = status
		self.name = name
		self.domain = domain
		self.user_id = user_id
		self.domain_id = domain_id
		for k in kwargs:
			setattr(self, k, kwargs[k])

	def __str__(self):
		return self.name
