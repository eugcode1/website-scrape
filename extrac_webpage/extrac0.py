#coding=gbk
import urllib2
from bs4 import BeautifulSoup
#unicode


url = 'http://wap.jjwxc.net/book2/785921/39'
req = urllib2.Request(url)  
response = urllib2.urlopen(req).read() 
response = unicode(response,'GBK').encode('UTF-8')
soup = BeautifulSoup(response.decode('utf-8'))
#remove all element tag
for script in soup.find_all('script'):
    script.extract()
for script in soup.find_all('form'):
    script.extract()
for script in soup.find_all('style'):
    script.extract()
for script in soup.find_all('img'):
    script.extract()
for script in soup.find_all('a'):
    script.extract()
#remove div by id
for div in soup.findAll('div', {"id": "logininfo"}):
    div.extract()
#remove li element with specific style
for div in soup.findAll('li', style="font-size: 12px; color: #009900;"):
    div.extract()
#remove vote section
for div in soup.findAll('font', {"id": "ticketsort"}):
    div.extract()
for div in soup.findAll('span', {"id": "ticketsortGap"}):
    div.extract()
soup_string = str(soup)
#replace text Chinese
s = '本文当前霸王票全站排行，还差 颗地雷就可以前进一名。'
s_gb =unicode(s,'GBK').encode('UTF-8')
soup_string = soup_string.replace(s_gb,"")

print s_gb

#print soup_string
text_file = open("C:\Users\PC\Desktop\Output.html", "w")
text_file.write("Novel content: %s" % soup_string)
text_file.close()
