import urllib.request
import re

urls = ["http://google.com","http://nytimes.com","http://cnn.com"]
i = 0
regex = b'<title>(.+?)</title>'
pattern = re.compile(regex)

while i<len(urls):
	htmlfile = urllib.request.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print (titles)
	i+=1