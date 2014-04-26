#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import urllib2

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)

def scrape_twitter(query):
	url = "https://twitter.com/search/realtime?q=%s&%s"%(query,"src=typd")
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)

	for instance in soup.find_all('p',{'class' : 'js-tweet-text'}):
		vine_url = instance.get_text()
		vine_url_array.append(vine_url)
		print remove_non_ascii(instance.get_text()) + '\n\n'

if __name__ == '__main__':
	try:
		scrape_twitter(sys.argv[1])
	except IndexError:
		print 'Specify query string as \n python main.py <query-string> \n'