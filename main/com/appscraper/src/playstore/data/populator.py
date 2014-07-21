__author__ = 'charles.bean'

""" Old Keys - beanchar : 'b476ea7e1a0c1dd3be9a845a1f889e44' """

import urllib.error
import urllib.request
import urllib.response
import urllib.parse
import json
from playstore.data.app import App


class Populator():

	def __init__(self):
		# HTTP Request and Response
		self.request = ''
		self.response = ''

		# URLs
		self.app_info_url = 'http://api.playstoreapi.com/v1.1/{0}/{1}?key={2}'
		self.search_api_url = 'http://api.playstoreapi.com/v1.1/search/{0}/{1}?key={2}'


	def getResponseAsDictionary(self, package_name, url, api='apps', api_key='5c907fec756a1ce39dbd1e354bb208fb'):
		"""
		Gets the response from the API server.
		Returns dictionary.
		:param package_name: str
		:param url: str
		:param api_key: str
		:return: dict
		"""
		if package_name and url:
			self.request = urllib.request.Request(url.format(api, package_name, api_key))  # Getting request from format str
			self.response = urllib.request.urlopen(self.request)  # Getting response from request string

			responseDict = json.loads(self.response.readall().decode('utf-8'))  # HttpRequest -> string -> dict

			print(responseDict)

			return responseDict
		else:
			raise ReferenceError('Missing Package Name or url')


	def searchAPI(self, search_term):
		"""
		Searches the API for apps with free text. Can search for all related to __.
		Returns dictionary.
		:param package_name: str
		:return: dict
		"""
		info = self.getResponseAsDictionary(search_term, self.search_api_url)
		return info


	def getAppInfo(self, package_name):
		"""
		Searches the API for an app and gets its information.
		Returns dictionary.
		:param package_name:
		:return: dict
		"""
		info = self.getResponseAsDictionary(package_name, self.app_info_url)
		return info


	def populateApps(self, app_list):
		"""
		Returns list of app objects.
		:param app_list:
		:raise Exception:
		"""
		try:
			if (app_list is type(list)):
				for app in app_list:
					new_app = App()

					# Adding search
					for key in app.keys():
						if key == 'itemID':
							new_app.item_ID = app[key]
						elif key == 'price':
							new_app.price = app[key]
						elif key == 'title':
							new_app.title = app[key]
						elif key == 'category':
							new_app.category = app[key]

					# Adding specifics
					if (new_app.item_ID):
						specifics = self.getAppInfo(new_app.item_ID)

						print(specifics)
			else:
				print('not a list')

			# if (dictionary['additionalInfo']):
			# 	try:
			# 		additional_info = dictionary['additionalInfo']
			# 		date_published = additional_info[0]['datePublished']
			#
			# 		self.published_date = date_published
			#
			# 	except Exception as ex:
			# 		raise Exception('populateApps was likely not passed a dictionary - {0}'.format(ex))
			#
			# else:
			# 	print ('No published date available for app - {0}'.format(dictionary))

		except Exception as ex:
			raise Exception('An Error occurred when calling populateApps - {0}\n\tDictionary - {1}'.format(ex, dictionary))
