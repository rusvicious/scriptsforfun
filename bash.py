#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import random, urllib2,re;

def getQuote():
	number = random.randrange(1,424243); 
	url =    "http://bash.im/quote/" + str(number);

	try:
		request = urllib2.Request(url);
                request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.0; rv:21.0) Gecko/20100101 Firefox/21.0');
                opener = urllib2.build_opener();
                data   = opener.open(request).read();	
                quote  = re.findall("<div class=\"text\">(.+)</div>",data);
                print(quote[0]);
    
        except urllib2.HTTPError, e:
    		if e.code != 200:
    			getQuote();

if __name__ == '__main__':
	getQuote();