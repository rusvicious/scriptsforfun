#!/usr/bin/env python
import random, urllib2

def getUrl():
	number = random.randrange(7600)
	url =    "http://media.oboobs.ru/boobs/0"+str(number)+".jpg"
	return url

def getBoobs(url):
	try:
    		urllib2.urlopen(url);
    		print(url)
    
    	except urllib2.HTTPError, e:
    		if e.code != 200:
    			getBoobs(getUrl())

if __name__ == '__main__':
	getBoobs(getUrl())