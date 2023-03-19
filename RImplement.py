# import subprocess

# res = subprocess.call("Rscript /Users/dradecic/Desktop/script.R", shell=True)
# res






import rpy2.robjects.packages as rpackages



utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1)
utils.install_packages('xml2')

from rpy2.robjects.packages import importr

rvest = importr('rvest')
xml2 = importr("xml2")
Rbase = xml2 = importr("base")

url = "https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876"

html = xml2.read_html(url)
dict(html[1])
xml2.xml_structure(html)

mtcars = data(datasets).fetch('mtcars')['mtcars']
mtcars


import requests
source = requests.get(url = url).text
n = source.find("<h1 ")

with open("a.txt", "w", encoding = "utf8") as f:
    f.write(s)
source



import urllib3
http = urllib3.PoolManager()
o = http.request('GET', url)
b = o.data
print(type(b))
s = b.decode("utf-8")
