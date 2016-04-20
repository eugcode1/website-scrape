#coding=gbk
import urllib2
from bs4 import BeautifulSoup
#unicode #for Chinese in ide 
save_path ="C:\Users\sandrac\Desktop\Output2.html"
save_path_txt ="C:\Users\sandrac\Desktop\Output2.txt"
book_title = "book name"
soup_string_all = ""
cha_start = 40
cha_end = 41
book_link = 'http://wap.jjwxc.net/book2/785921/'
#Scrape begin
for num in range(cha_start,cha_end+1):
    soup = ""
    soup_string = ""
    url = book_link +str(num)
    req = urllib2.Request(url)  
    response = urllib2.urlopen(req).read() 
    response = unicode(response,'GBK').encode('UTF-8')
    soup = BeautifulSoup(response.decode('utf-8'),"html.parser")
    #remove all element tag
    for script in soup.find_all('script'):
        script.extract()
    for script in soup.find_all('form'):
        script.extract()
    for script in soup.find_all('style'):
        script.extract()
    for script in soup.find_all('link'):
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
    #might not need remove extra space after parsling
    soup_string = soup_string.replace("</br>","")
    #replace all li with inline style
    soup_string = soup_string.replace("<li>",'<ul style = "list-style-type: none;">')
    soup_string_all += soup_string
    print "chapter: %d is done" %num

#save into a html docu
html_file = open(save_path, "w")
html_file.write(book_title + "<br>")
html_file.write(soup_string_all)
html_file.close()

#convert from html to txt
'''
soup = BeautifulSoup(soup_string_all)
for script in soup.find_all('title'):
        script.extract()
for e in soup.find_all("head"):
    e.extract()

a_tag = soup.br
new_tag = soup.new_tag("p")
a_tag.replace_with(new_tag)
print soup
txt_str = soup.get_text()
#convert to utf-8 to be saved in txtfile
txt_str = txt_str.encode('utf-8')
txt_file = open(save_path_txt, "w")
txt_file.write(txt_str)
txt_file.close()
'''
print "Book Extraction Done"
