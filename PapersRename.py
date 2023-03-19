import requests
from bs4 import BeautifulSoup
 
# target url
url = 'https://www.sciencedirect.com/science/article/pii/S0731708519316590'
 
# making requests instance
reqs = requests.get(url)
 
# using the BeautifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')
 
# displaying the title
print("Title of the website is : ")
for title in soup.find_all('citation_title'):
    print(title)
    


url = ""
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen(url)
bsh = BeautifulSoup(html.read(), 'html.parser')
print(bsh.h1)



from selenium import webdriver

browser = webdriver.Edge()
browser.get('chrome://newtab')
content = browser.page_source
browser.close()
n = content.find("neusilin")
content[n-100:n+100]



from nltk import clean_html   
from urllib import urlopen

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
html = urlopen(url).read()    
raw = clean_html(html)  
print(raw)



import urllib.request

opener = urllib.request.FancyURLopener({})
url = "http://stackoverflow.com/"
f = opener.open(url)
content = f.read()


import urllib2
url = "http://somewhere.com"
page = urllib.urlopen(url)
data = page.read()
print dat





import sys
import pycurl

class ContentCallback:
        def __init__(self):
                self.contents = ''

        def content_callback(self, buf):
                self.contents = self.contents + buf

t = ContentCallback()
curlObj = pycurl.Curl()
curlObj.setopt(curlObj.URL, 'http://www.google.com')
curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
curlObj.perform()
curlObj.close()
print t.contents

import urllib.request    
urllib.request.urlretrieve(url, "test.txt")

