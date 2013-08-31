#!/usr/bin/python
import random, webbrowser;

def getBoobs():
	number = random.randrange(7600); 
	url =    "http://media.oboobs.ru/boobs/0"+str(number)+".jpg"
	webbrowser.open_new(url);

getBoobs();