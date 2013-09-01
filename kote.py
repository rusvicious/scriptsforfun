#!/usr/bin/env python
import random, urllib2,re;

def getKote():
	number = random.randrange(353); 
	url =    "http://kote-img.com/" + str(number);

	try:
		response = urllib2.urlopen(url);
    		data = response.read();	
    		matches  = re.findall(".*media/kotes/.*",data);
    		kote  = re.findall("src=\"(.+)\"",matches[0]);
    		print("http://kote-img.com"+kote[0]);
    
    	except urllib2.HTTPError, e:
    		if e.code != 200:
    			getKote();

	

if __name__ == '__main__':
	getKote();