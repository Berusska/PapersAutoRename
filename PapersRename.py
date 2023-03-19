from bs4 import BeautifulSoup
import pyperclip as pc
import pyautogui
import time

pyautogui.hotkey('ctrl', 'u') 
time.sleep(1) 
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






