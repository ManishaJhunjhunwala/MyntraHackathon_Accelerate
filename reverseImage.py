#import pysftb as sftp

import urllib.request as urllib2
from urllib.request import Request, urlopen
from http.cookiejar import CookieJar
import re
import time

cj= CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

def imageLookup():
#	s = sftp.Connection(host = "pythonprogramming.net",
#		username = "python", password = "rules")
#	localpath = '/hone/pi/imagerec/currentimage.jpg'
#	numToAdd = str(int(time.time()))
#	remotepath = '/var/www/imagerec/currentimage'+numToAdd+',jpg'
#	s.put(localpath, remotepath)
#	s.close()
	
	
	imagepath = 'https://www.pinterest.es/pin/223843043967354433/'
	googlepath = 'http://google.com/searchbyimage?image_url='+imagepath
	
	#sourceCode = opener.open(googlepath).read()
	
	url = "https://stackoverflow.com/questions?page=298314" + "&sort=active"    

	req = Request(imagepath, headers={'User-Agent': 'Mozilla/5.0'})    
	html = urlopen(req).read()
	
	findlinks = re.findall(r'<div class = "rg_meta">{"os":".*?","cb":.*?,"ou":"(.*?)","rh":"',str(html))
	for eachThing in findlinks:
		print(eachThing)
	
	f = open("reverseImageHtmlCode.txt", "a")
	f.write(str(html))
	f.close()
	
	print(html)
	

imageLookup()
