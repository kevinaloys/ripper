import requests
from bs4 import BeautifulSoup
import re
import os
from ripper import utils
import shutil

class ripper(object):

    def __init__(self, name = 'ripper'):
        self.urls = []
        self.text = None
        self.name = name
        self.soup = None

    def __repr__(self):
        return('<Type: ripper, Name: {}>'.format(self.name))     


    def get(self, url, format = 'jpg'):
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        self.soup = soup
        all_url = []
        for link in soup.find_all('img'):
            all_url.append(link.get('src'))
        for url in all_url:
            format = utils.vertical_to_comma(format)
            if re.match('.+\.({})'.format(format), url):
                self.urls.append(url)


    def save(self, to = None):
        if to == None:
            basedir = os.getcwd()
            if not os.path.isdir(self.soup.title.string):
                os.makedirs(self.soup.title.string)
        os.chdir(self.soup.title.string)
        for each_url in self.urls:
            r = requests.get(each_url, stream = True)
            with open(utils.image_name(each_url), 'wb') as outfile:
                shutil.copyfileobj(r.raw, outfile)
            del r