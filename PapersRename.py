
# https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876
url = "https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876"



from urllib.parse import urlparse
web = urlparse("https://link.springer.com/article/10.1007/s00204-016-1827-3")
web = urlparse("https://www.researchgate.net/publication/11211492_Influence_of_the_drying_technique_on_theophylline_pellets_prepared_by_extrusion-spheronization")
web.scheme
web.netloc #
web.hostname




from pathlib import Path
from pyquery import PyQuery 
import pyperclip as pc
import time
import keyboard
import PySimpleGUI as sg
import pyautogui



def downloadOpenPDF():
    pyautogui.click(0, 200)
    pyautogui.hotkey('ctrl', 's')#takže by mělo stačit jen zkopírovat F6; Ctrl + C 
    pyautogui.click(100, 200) # stahovací okno musí mít určitou pozici
    pyautogui.hotkey("enter") #na zavření dialogi stahování
    pyautogui.click(100, 200) # AKTIVACE TABU
    pyautogui.hotkey("ctrl", "w") #zavření tabu


def downloadSciencePDF():
    ...

def getTitle():
    pyautogui.hotkey('ctrl', 'u') # TODO: pak url =  view-source:https://link.springer.com/article/10.1007/s00204-016-1827-3
    time.sleep(0.5) 
    pyautogui.hotkey('ctrl', 'a')  
    pyautogui.hotkey('ctrl', 'c')  
    pyautogui.hotkey('ctrl', 'w') 
    htmlWebu = pc.paste() 
    
    pq = PyQuery(htmlWebu)
    tag = pq('title') # or     tag = pq('div.class')
    Titul = tag.text()
    return Titul
    
def FileOccured():
    ...
    
def Rename():
    ...


def userIO():
    pc.copy("0"); predtim = "0"

    klavesa = keyboard.read_key()
    
    if klavesa == "esc":
        print("Uživatelem vyžádaný konec programu")
        sg.popup_auto_close("KONEC PROGRAMU.", background_color="darkgreen" ,auto_close_duration=1, keep_on_top=True, )
        pyautogui.click(100, 200) #na zavření tabu
        pyautogui.hotkey('ctrl', 'w')  
        return 0               
    elif klavesa == "f9": #PRO ELSEVIER ETC.
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
        
        # downloadSciencePDF() 
        #TODO: tady to stahování zatím nech být - bude to možná komplikovaný, zajisti jen to přejmenování
        
        name = getTitle()
        
        if FileOccured():
            Rename(name)
        
        
        return "continue"
        
    elif klavesa == "f8": #pro další bezejmenná otevřená pdf
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
    
        if predtim != schranka:
            downloadOpenPDF()
            predtim = schranka
            
            return "continue"
        
    elif klavesa == "f6": #pro již stažená (nepohlídané vědecké portály)
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
    else: pass #není zmážknuta klávesa, nebo je jiná od definovaných

    # nazev = getTitle()
    # web = ...
    # if web in ["link.springer.com", "www.researchgate.net", ...]:
    #     # downloadPDF()
        
    # if novyFile():
    #     Rename()

    



def main():
    primSlozka = Path.cwd()
    sekSlozka = Path("./downloaded")
    sekSlozka.mkdir(parents=True, exist_ok=True)

    veSlozce = set(sorted(primSlozka.glob("*.pdf"))) 

    with open("querys.txt", "r", encoding="utf-8") as f:
        urls = f.read().splitlines()
    
    while True:
        output = userIO()
        if output == 0:
            break
    
        
        