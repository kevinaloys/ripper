import requests
from bs4 import BeautifulSoup
import re
import os
import utils

class ripper(object):

    def __init__(self):
    	self.urls = []
    	self.text = None

    def __repr__(self):
    	return('<Type: ripper>')

    def get(self, url, format = 'jpg, gif, png'):
    	r = requests.get(url)
    	soup = BeautifulSoup(r.text)
    	all_url = []
    	for link in soup.find_all('img'):
    		all_url.append(link.get('src'))
    	for url in all_url:
    		format = utils.vertical_to_comma(format)
    		if re.match('.+\.({})'.format(format),url):
    			self.urls.append(url)