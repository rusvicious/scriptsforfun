#!/usr/bin/python
import random, webbrowser, urllib2;

def getUrl():
	number = random.randrange(7600); 
	url =    "http://media.oboobs.ru/boobs/0"+str(number)+".jpg"
	return url;

def getBoobs(url):
	result = 1;
	try:
    		urllib2.urlopen(url);
    		webbrowser.open_new(url);
    
    	except urllib2.HTTPError, e:
    		if e.code != 200:
    			getBoobs(getUrl());

getBoobs(getUrl());