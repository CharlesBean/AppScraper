__author__ = 'KingChawles'

import urllib.error
import urllib.request
import urllib.response
import urllib.parse
import json

class Information:
	def __init__(self):
		self.app_name = ''
		self.request = ''
		self.response = ''

		self.app_info_url = 'http://api.playstoreapi.com/v1.1/{0}/{1}?key={2}'
		self.search_api_url = 'http://api.playstoreapi.com/v1.1/search/{0}/{1}?key={2}'


	def getInfo(self, package_name, url, api='apps', api_key='b476ea7e1a0c1dd3be9a845a1f889e44'):
		"""
		Gets the response from the API server

		:param package_name: str
		:param url: str
		:param api_key: str
		:return: str
		"""
		if package_name:
			self.request = urllib.request.Request(url.format(api, package_name, api_key)) # Getting request from format str
			self.response = urllib.request.urlopen(self.request) # Getting response from request string

			self.response = self.response.readall().decode('utf-8') # Have to decode - bytes

			return self.response
		else:
			raise ReferenceError('Missing Package Name')


	def searchAPI(self, package_name):
		"""
		Searches the API for apps with free text. Can search for all related to __.

		:param package_name: str
		:return: str
		"""
		info = self.getInfo(package_name, self.search_api_url)
		return info


	def getAppInfo(self, package_name):
		"""
		Searches the API for an app and gets its information.

		:param package_name:
		:return:
		"""
		info = self.getInfo(package_name, self.app_info_url)
		return info


def main():
	info = Information()
	info.searchAPI('ford')

	print(info.response)

	for app in info.response:
		print(app[0])


main()
