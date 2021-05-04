import os
from json import JSONDecodeError
from urllib.parse import urlencode

import requests
from requests import Response


class Arvan:
	def __init__(self, api_key: str = None):
		if api_key:
			self.api_key = api_key
		else:
			self.api_key = os.environ.get('AR_API_KEY')

	def _build_headers(self, headers: dict = None) -> dict:
		assert self.api_key, 'API KEY must be provided.'
		if not headers:
			headers = {}
		base_headers = {'AUTHORIZATION': self.api_key}
		headers = {**headers, **base_headers}
		return headers

	def _render_response(self, response: Response):

		try:
			if 'data' in response.json():
				return response.json().get('data')
			return response.json()
		except JSONDecodeError:
			return response

	def _send_request(self, method: str, url: str, data: dict = None, json: dict = None, query_params: dict = None,
					  headers: dict = None):
		headers = self._build_headers(headers)
		if method.lower() == 'get':
			if query_params and len(query_params):
				url = url + '?%s' % (urlencode(query_params))
			r = requests.get(url, headers=headers)
			return self._render_response(r)
		if method.lower() == 'post':
			if data and json:
				raise ValueError('only one of data and json is allowed.')
			r = requests.post(url, headers=headers, data=data, json=json)
			return self._render_response(r)

	def send_request(self, method: str, url: str, data: dict = None, query_params: dict = None):
		return self._send_request(method, url, data, query_params)
