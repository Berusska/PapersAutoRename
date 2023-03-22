from bs4 import BeautifulSoup
import pyperclip as pc
import pyautogui
import time
import keyboard
import PySimpleGUI as sg


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



from urllib.parse import urlparse
web = urlparse("https://link.springer.com/article/10.1007/s00204-016-1827-3")
web = urlparse("https://www.researchgate.net/publication/11211492_Influence_of_the_drying_technique_on_theophylline_pellets_prepared_by_extrusion-spheronization")
web.scheme
web.netloc #
web.hostname




from pathlib import Path


primSlozka = Path.cwd()
sekSlozka = Path("./downloaded")
sekSlozka.mkdir(parents=True, exist_ok=True)

with open("querys.txt", "r", encoding="utf-8") as f:
    querys = f.read().splitlines()

print("zadaných querys bylo: ", len(querys))


def downloadPDF():
    ...

def getTitle():
    ...
    
def Rename():
    ...


def userIO():
    klavesa = keyboard.read_key()
    
    if klavesa == "esc":
        print("Uživatelem vyžádaný konec programu")
        sg.popup_auto_close("KONEC PROGRAMU.", background_color="darkgreen" ,auto_close_duration=1, keep_on_top=True, )
        pyautogui.click(100, 200) #na zavření tabu
        pyautogui.hotkey('ctrl', 'w')  
        return 0               
    elif klavesa == "f9": #PRO 
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        
    elif klavesa == "f8": 
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
    
        if predtim != schranka:
            pyautogui.click(0, 200)
            pyautogui.hotkey('ctrl', 's')#takže by mělo stačit jen zkopírovat F6; Ctrl + C 
            pyautogui.click(100, 200) # stahovací okno musí mít určitou pozici
            pyautogui.hotkey("enter") #na zavření dialogi stahování
            predtim = schranka
            indikace_schranky = 1 

    nazev = getTitle()
    web = ...
    if web in ["link.springer.com", "www.researchgate.net", ...]:
        downloadPDF()
        
    if novyFile():
        Rename()

    



def main():
    while True:
        output = userIO()
        if output == 0:
            break
    
        
        