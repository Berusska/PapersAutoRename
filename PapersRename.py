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














from newspaper import Article
from newspaper3k import Article

article = Article(url)
article.download()
article.parse()
article.text



import pandas as pd

http = r'https://www.ibm.com/docs/en/cmofz/10.1.0?topic=SSQHWE_10.1.0/com.ibm.ondemand.mp.doc/arsa0257.htm'
table = pd.read_html(url)







from lxml import html
import requests

page = requests.get(url)
tree = html.fromstring(page.content)




















import subprocess

res = subprocess.call("Rscript /Users/dradecic/Desktop/script.R", shell=True)
res



from rpy2 import robjects

pi = robjects.r['pi']
pi


robjects.r('''
    add_nums <- function(x, y) {
        return(x + y)
    }
    
    print(add_nums(x = 5, y = 10))
    print(add_nums(x = 10, y = 20))
''')


import rpy2.robjects.packages as rpackages


utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)

utils.install_packages('<package_name>')


from rpy2.robjects.packages import importr, data

datasets = importr('datasets')
mtcars = data(datasets).fetch('mtcars')['mtcars']
mtcars