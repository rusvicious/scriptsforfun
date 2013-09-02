#!/usr/bin/env python

import sys;
import random, urllib2, re, time;

def replaceHTML(string):
	str = string.replace("<br>","\n");
	str = str.replace("<br />","\n");
	str = str.replace("&quot;","\"");
	str = str.replace("&gt;",">");
	str = str.replace("&lt;","<");
	return str;
	
def getQuote():
	url =    "http://bash.im/random";
	charset = "utf-8";
	
	if sys.platform == "win32":
		charset = "cp866";
		
	try:
		request = urllib2.Request(url);
		request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.0; rv:21.0) Gecko/20100101 Firefox/21.0');
		opener = urllib2.build_opener();
		data   = opener.open(request).read();	
		quote  = re.findall("<div class=\"text\">(.+)</div>",data);
		text   = replaceHTML(quote[random.randrange(0,len(quote)-1)]);
		print(unicode(text,"cp1251").encode(charset)+"\n-------------------------------------------------\n");
				    
	except urllib2.HTTPError, e:
		if e.code != 200:
			getQuote();

if __name__ == '__main__':
	while True:
		getQuote();
		time.sleep(30);