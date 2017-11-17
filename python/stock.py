import urllib.request
import re

htmlfile = urllib.request.urlopen("https://in.finance.yahoo.com/quote/AAPL?p=AAPL")
htmltext = htmlfile.read().decode('iso-8859-1')
with open('stock.txt','w',encoding='utf-8') as f:
	f.write(htmltext)

regex = '<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)">(.+?)</span>'
file = open('stock.txt')
pattern = file.read()
print(pattern)
price = re.findall(pattern, htmltext)

print(price)
