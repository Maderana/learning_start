from urllib.request import urlopen
import re

#connect to a URL
website = urlopen("https://github.com/search?utf8=%E2%9C%93&q=web+scraping&type=")

#read html code
html = website.read().decode('utf-8')

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)

print (links)