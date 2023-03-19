
library(rvest)

url = "https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876"
scraping_wiki <- read_html(url)

x <- scraping_wiki %>%
  html_nodes("HEAD")
print(x[[1]])


library(xml2)
write_xml(scraping_wiki, file="temp.html")


jakotext <- as.character(scraping_wiki)



for (i in 1:23){print(x[[i]])}

file.rename()


write.table(scraping_wiki[["<head>"]], "a.txt")
typeof(scraping_wiki)


#https://www.r-bloggers.com/2022/03/how-to-use-r-and-python-together-try-these-2-packages/


library(RCulr)
library(XML)
# download html
html <- getURL(url, followlocation = TRUE)
# parse html
doc = htmlParse(html, asText=TRUE)


library(rvest)
library(XML)

pg <- html("http://dds.ec/")
saveXML(pg, "output.html")



xml_structure()
