#!/usr/bin/env python
import sys;
import random, urllib2, re;

def getQuote():
	number = random.randrange(1,843); 
	url =    "http://bash.im/index/" + str(number);
	charset = "utf-8";
	
	if sys.platform == "win32":
		charset = "cp866";
		
	try:
		request = urllib2.Request(url);
                request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.0; rv:21.0) Gecko/20100101 Firefox/21.0');
                opener = urllib2.build_opener();
                data   = opener.open(request).read();	
                quote  = re.findall("<div class=\"text\">(.+)</div>",data);
                print(unicode(quote[random.randrange(0,len(quote)-1)],"cp1251").encode(charset).replace("<br>","\n"));
    
        except urllib2.HTTPError, e:
    		if e.code != 200:
    			getQuote();

if __name__ == '__main__':
	getQuote();