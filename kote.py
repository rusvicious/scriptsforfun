#!/usr/bin/env python
import random, urllib2;

def getUrl():
	number = random.randrange(353); 
	url =    "http://kote-img.com"
	return url;

def getKote(url):
	try:
    		urllib2.urlopen(url);
    		print(url);
    
    	except urllib2.HTTPError, e:
    		if e.code != 200:
    			getKote(getUrl());

if __name__ == '__main__':
	getBoobs(getUrl());