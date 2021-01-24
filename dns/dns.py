import logging

from arvan.api import Arvan
from dns.domain import Domain


class DNS(Arvan):
	get_domains_url = 'https://napi.arvancloud.com/cdn/4.0/domains'

	def get_domains(self, query_params: dict = None):
		r = self._send_request('GET', self.get_domains_url, query_params)
		logging.error(r)
		return [Domain(**x) for x in r['data']]
