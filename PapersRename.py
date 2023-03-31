
# https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876
# url = "https://www.sciencedirect.com/science/article/abs/pii/S1359511308001876"
# https://link.springer.com/article/10.1007/s00204-016-1827-3
# https://www.researchgate.net/publication/11211492_Influence_of_the_drying_technique_on_theophylline_pellets_prepared_by_extrusion-spheronization


from pathlib import Path
from pyquery import PyQuery 
import pyperclip as pc
import time
import keyboard
import PySimpleGUI as sg
import pyautogui
import re
import textwrap
from urllib.parse import urlparse


import colorama



def downloadOpenPDF():
    pyautogui.click(0, 200)
    pyautogui.hotkey('ctrl', 's')#takže by mělo stačit jen zkopírovat F6; Ctrl + C 
    pyautogui.click(100, 200) # stahovací okno musí mít určitou pozici
    pyautogui.hotkey("enter") #na zavření dialogi stahování
    pyautogui.click(100, 200) # AKTIVACE TABU
    pyautogui.hotkey("ctrl", "w") #zavření tabu


def downloadSciencePDF():
    ...  #TODO: zatím nechat

def getTitle():
    pyautogui.hotkey('ctrl', 'u') # pak lze url =  view-source:https://link.springer.com/article/10.1007/s00204-016-1827-3
    time.sleep(1) 
    pyautogui.click(100, 200)
    pyautogui.hotkey('ctrl', 'a')  
    pyautogui.hotkey('ctrl', 'c')  
    pyautogui.hotkey('ctrl', 'w') 
    htmlWebu = pc.paste() 
    print("\tZiskán html kod.")
    
    pq = PyQuery(htmlWebu)
    print("\thtml:" + htmlWebu[0:60])
    tag = pq('title') # or     tag = pq('div.class')
    print("\ttag:" + str(tag))
    Titul = tag.text()
    print("\ttitul: " + Titul)
    return Titul
    
def FileOccured(veSlozce: any):
    veSlozce_actual = set(sorted(primSlozka.glob("*.pdf")))
    newFile = veSlozce.symmetric_difference(veSlozce_actual)
    if len(newFile) != 0:
        cestaFile = list(newFile)[0]
        print(f"\t{cestaFile.name}")
        return (True, cestaFile, veSlozce_actual)
    else: 
        return (False, None, None)
    
def Rename(cestaFile: Path, titul: str):
    nazevPresunu = re.sub("[:!?*;°/\\\\]","_", titul)
    print(f"\t{nazevPresunu}")
    celaCesta = str(sekSlozka.absolute()) + "/" + nazevPresunu + cestaFile.name
    if len(celaCesta) >150:
        celaCesta = celaCesta[0:150] + ".pdf"
        
    try:
        cestaFile.rename(celaCesta)
        print("\tPokus souboru o přejmenování.")
        if Path(celaCesta).exists():
            print("\tSoubor byl přesunut.")
        else: print("CHYBA !!!")
        indikace_schranky = 0
    except:
        FileExistsError

def hlaseniKonce():
    layout = [[sg.Text(text='Byla stisknuta klávesa Esc.\n\nProgram byl ukončen uživatelem.', font=('Arial Bold', 20), background_color="indigo")]]
    hlaseni = sg.Window("Konec programu.", layout,auto_close_duration=1, keep_on_top=True, size=(715,250), finalize=True, auto_close=True, background_color="indigo")

    hlaseni.read()
    
def hlaseniSouboru(newFile: Path, schranka: str, titul: str):
    cestaFile = list(newFile)[0]
    print(f"\t{cestaFile.name}")
    schrana = textwrap.fill(schranka, 70).replace("\n", "\n\t")

    layout = [[sg.Text(f"Ve schránce je nová url adresa a zároveň se objevil nový PDF soubor v primární složce.\n\n\tNový soubor: {cestaFile.name}\n\n\tObsah schránka: {schrana}\n")],
              [[sg.Button('V pořádku', size = (15, 2), pad=((15,20),20), button_color="green"), sg.Button('Špatně\nUprava uživatelem', size = (15, 2), pad=((15,20),20), button_color="red")]]]
    
    # schranka = pc.paste() #joko možnost opravy v průběhu
    
    schvaleni, other = sg.Window('Stahování zdrojů pro DP', layout, keep_on_top=True, size=(715,250), finalize=True, auto_close=True, background_color="indigo").read(close=True) 
    
    if schvaleni == 'Stahování zdrojů pro DP':
        return True
    else: 
        return False

def UpravaUzivatelem():
    print("Uprava uživatelem zatím není podporovaná.")
    ... #TODO:
    
    
def SciencePortal(urlAdresa: str):
    web = urlparse(urlAdresa)
    domena = web.scheme
    
    # web.netloc 
    # web.hostname
    
    if domena in ["https://link.springer.com", "https://www.sciencedirect.com", "https://www.researchgate.net"]:
        return True
    else:
        return False


def userIO():
    pc.copy("0"); predtim = "0"

    klavesa = keyboard.read_key()
    
    if klavesa == "esc":
        print("Uživatelem vyžádaný konec programu")
        hlaseniKonce()
        pyautogui.click(100, 200) #na zavření tabu
        pyautogui.hotkey('ctrl', 'w')  
        return (0, None, None)  #vede ke konci programu              
    elif klavesa == "f9": #PRO ELSEVIER ETC. #TODO: místo uživatelsky volenou klávesou by se mohla název stránky: jestli bude náležet do množiny, pak to pojede podle následujícího kódu -> -> -> fce SciencePortal()
        print("\tStisknuta F9")
        pyautogui.click(100, 200)
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
        
        # downloadSciencePDF() 
        #TODO: tady to stahování zatím nech být - bude to možná komplikovaný, zajisti jen to přejmenování
        
        name = getTitle()
        print("\tZiskan titul ")
        print(name)
        
        while True:
            newFile = FileOccured(veSlozce = veSlozce)
            
            if newFile[0]:
                # veSlozce = newFile[2]
                print("\tNalezen nový soubor: " + str(newFile[1]))
                schvaleni = hlaseniSouboru(newFile = newFile, schranka = schranka, titul=name)
                
                if schvaleni:
                    Rename(newFile[1], name)
                else:
                    UpravaUzivatelem()
                                
                break
                    
        return ("continue", newFile[2] )# vede k pokračování programu
        
    elif klavesa == "f8": #pro další bezejmenná otevřená pdf
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
    
        if predtim != schranka:
            downloadOpenPDF()
            predtim = schranka
            
            return ("continue", None) #TODO: nahradit None
        
    elif klavesa == "f6": #pro již stažená (nepohlídané vědecké portály)
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
    else: pass #není zmážknuta klávesa, nebo je jiná od definovaných

    
    #TODO: zajistit průběžný záznam práce do urls.txt


def main():
    print("\033[91m" + "Skript byl spuštěn." + "\033[0m")
    while True:
        output = userIO()
        if output[0] == 0:
            break
        else:
            veSlozce = output[1]
    
    print("Vystoupení z while-loopu. Konec programu")
    
        
if __name__ == "__main__":
    colorama.init()

    primSlozka = Path.cwd()
    sekSlozka = Path("./downloaded")
    sekSlozka.mkdir(parents=True, exist_ok=True)

    veSlozce = set(sorted(primSlozka.glob("*.pdf"))) 
    
    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = f.read().splitlines()
    
    main()
    
    
    
#FIXME: https://pypi.org/project/PySimpleGUI/4.17.0/
# TODO: sg.InputText() S DEFINOVANOU HODNOTOU
# https://github.com/PySimpleGUI/PySimpleGUI/issues/966

#https://www.activestate.com/resources/quick-reads/how-to-install-python-packages-using-a-script/# https://stackoverflow.com/questions/74154603/how-to-add-a-field-in-one-text-input-by-clicking-a-button-in-pysimplegui

#https://www.reddit.com/r/learnpython/comments/mosgc5/updating_text_with_pysimplegui/




#TODO: na začátku nechat uživatel ekliknout na ikonku Zotera v pc; do RunProgram dát příkaz na spuštění Zotera