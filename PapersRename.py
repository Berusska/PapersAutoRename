from bs4 import BeautifulSoup
import pyperclip as pc
import pyautogui
import time

# https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876
url = "https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876"



pyautogui.hotkey('ctrl', 'u') # TODO: pak url =  view-source:https://link.springer.com/article/10.1007/s00204-016-1827-3
time.sleep(0.5) 
pyautogui.hotkey('ctrl', 'a')  
pyautogui.hotkey('ctrl', 'c')  
pyautogui.hotkey('ctrl', 'w')  

html = pc.paste()


#buď
start = html.find("""<meta name="citation_title" content=""") + 36
konec = html[start:].find(" />")
html[start:start+konec]


#nebo
start = html.find("<title>") + 7
konec = html.find("</title>")
html[start:konec]

pyautogui.click(100, 200) #na zavření tabu
pyautogui.hotkey('ctrl', 'w')  

#anebo
soup = BeautifulSoup(html, 'html.parser')

print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title)

soup.find_all('title')[0].text



#alebo
from pyquery import PyQuery 
pq = PyQuery(html)
tag = pq('title') # or     tag = pq('div.class')
print(tag.text())

