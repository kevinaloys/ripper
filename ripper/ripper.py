import requests
from bs4 import BeautifulSoup
import re

class ripper(object):

	def __init__(self):
		self.urls = []
		self.text = None

	def __repr__(self):
		return('<Type: Ripper Object>')

	def get(self, url, type='jpg|gif'):
		r = requests.get(url)
		soup = BeautifulSoup(r.text)
		all_url = []
		for link in soup.find_all('img'):
			all_url.append(link.get('src'))
		for url in all_url:
			if re.match('.+\.({})'.format(type),url):
				self.urls.append(url)

	
def main():
	d = ripper()
	d.get('http://www.facebook.com')
	print(d.urls)
if __name__ =='__main__':
	main()