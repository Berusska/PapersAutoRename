
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
import fitz
import pywhatkit


import colorama

colorama.init()
theme = "Darkgreen"
font_family = "Comic Sans MS"
font_size = int(10)
sg.theme(theme)
sg.set_options(font=(font_family, font_size))

primSlozka = Path.cwd()
sekSlozka = Path("./downloaded")
sekSlozka.mkdir(parents=True, exist_ok=True)

veSlozce = set(sorted(primSlozka.glob("*.pdf"))) 

with open("urls.txt", "r", encoding="utf-8") as f:
    urls = f.read().splitlines()



def downloadOpenPDF():
    pyautogui.click(0, 200)
    pyautogui.hotkey('ctrl', 's')#takže by mělo stačit jen zkopírovat F6; Ctrl + C 
    pyautogui.click(100, 200) # stahovací okno musí mít určitou pozici
    pyautogui.hotkey("enter") #na zavření dialogi stahování
    pyautogui.click(100, 200) # AKTIVACE TABU
    pyautogui.hotkey("ctrl", "w") #zavření tabu


def downloadSciencePDF():
    ...  #TODO: zatím nechat

def getTitle(science : bool):
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
    layout = [[sg.Text(text='Byla stisknuta klávesa Esc.\n\nProgram byl ukončen uživatelem.', font=('Arial Bold', 14), background_color="blue")]]
    hlaseni = sg.Window("Konec programu.", layout,auto_close_duration=1, keep_on_top=True, size=(500,100), finalize=True, auto_close=True, background_color="blue")

    hlaseni.read()
    

def hlaseniSouboru(newFile: Path, schranka: str, titul: str):
    print(f"\t{newFile.name}")
    
    # Load the first page of the PDF file
    pdf_file = newFile
    doc = fitz.open(pdf_file)
    page = doc.load_page(0)

    # Convert the page to an image buffer
    # pixmap = page.get_pixmap()
    # img_bytes = pixmap.tobytes()
    
    resolution = 60

    # Get the pixmap with the desired resolution
    mat = fitz.Matrix(resolution / 72.0, resolution / 72.0)
    pix = page.get_pixmap(matrix=mat)

    # Convert the pixmap to bytes
    img_bytes = pix.tobytes()


    
    # ------ GUI Definition ------ #
    pdfviewer = [[sg.Image(data=img_bytes)]]
    formular = [[sg.T("Nový soubor:", s=11, justification="r"), sg.Multiline(size = (40, 5), key="-IN-", default_text=newFile.name), sg.FolderBrowse()], [sg.T("Obsah schranky:", s=11, justification="r"), sg.Multiline(size = (40, 5), key="-OUT-", default_text=schranka)], [sg.T("Titul:", s=11, justification="r"), sg.Multiline(size = (40, 5), key="-TIT-", default_text=titul)], [sg.Exit(s=16, button_color="tomato"), sg.B("V pořádku", size = (15, 2), pad=((15,20),20), button_color="green")]]

    layout = [[sg.Text(f"Ve schránce je nová url adresa a zároveň se objevil nový PDF soubor v primární složce.\n")], [sg.Column(pdfviewer), sg.VSeperator(), sg.Column(formular)]]
    window = sg.Window("GUI", layout, alpha_channel=0.99, grab_anywhere=True, location=(0,0))

    while True:
        event, values = window.read()
        print(event)
        print(values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event in ("Command 1", "Command 2", "Command 3", "Command 4"):
            sg.popup_error("Not yet implemented")
        if event == "V pořádku":
            if is_valid_path(values["-IN-"]):
                Rename(newFile, values["-TIT-"])

    window.close()
    
def SciencePortal(urlAdresa: str):
    web = urlparse(urlAdresa)
    domena = web.scheme
    
    # web.netloc 
    # web.hostname
    
    if domena in ["https://link.springer.com", "https://www.sciencedirect.com", "https://www.researchgate.net"]:
        return True
    else:
        return False

def Zotero(pos):
    pyautogui.click(pos)
    time.sleep(1)

def userIO(pos):
    pc.copy("0"); predtim = "0"
    klavesa = keyboard.read_key()
    
    if klavesa == "esc":
        print("Uživatelem vyžádaný konec programu")
        hlaseniKonce()
        pyautogui.click(100, 200) #na zavření tabu
        pyautogui.hotkey('ctrl', 'w')  
        quit()

    elif klavesa == "f9":
        print("\tStisknuta F9")
        pyautogui.click(100, 200)
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
        

        name = getTitle(SciencePortal(schranka))
            #TODO: tady to stahování zatím nech být - bude to možná komplikovaný, zajisti jen to přejmenování

        print("\tZiskan titul ")
        print(name)
        
        while True:
            newFile = FileOccured(veSlozce = veSlozce)
            
            if newFile[0]:
                # veSlozce = newFile[2]
                print("\tNalezen nový soubor: " + str(newFile[1]))
                hlaseniSouboru(newFile = newFile[1], schranka = schranka, titul=name)
                break
                    
        return newFile[2]# vede k pokračování programu
        
    elif klavesa == "f8": #pro další bezejmenná otevřená pdf
        pyautogui.hotkey('f6')
        pyautogui.hotkey('ctrl', 'c')    
        schranka = pc.paste()
    
        if predtim != schranka:
            downloadOpenPDF()
            predtim = schranka
            
            while True:
                newFile = FileOccured(veSlozce = veSlozce)
                
                if newFile[0]:
                    # veSlozce = newFile[2]
                    print("\tNalezen nový soubor: " + str(newFile[1]))
                    hlaseniSouboru(newFile = newFile[1], schranka = schranka, titul="Soubor")
                    break
            
            return newFile[2]
        

    
    #TODO: zajistit průběžný záznam práce do urls.txt

def is_valid_path(filepath):
    if filepath and Path(filepath).exists():
        return True
    
    sg.popup_error("Filepath not correct")
    return False

def NajdiZotero():
    print("Najeďtě myší na ikonku Zotera ve svém prohlížeči. \nPonechte kurzor myši na ikoně a stiskněte klavesu CTRL, program bude pokračovat...")
    pywhatkit.search("www.google.com")
    while True:
        pos = pyautogui.position()
        klavesa = keyboard.read_key()
        if klavesa == "ctrl":
            print(f"Byla zjištěna poloha ikonky Zotera: {pos}.\n\nNyní můžete pracovat.")
            break
    
    return pos


if __name__ == "__main__":
    print("\033[91m" + "Skript byl spuštěn." + "\033[0m")
    pos = NajdiZotero()
    while True:
        userIO(pos)
        veSlozce = set(sorted(primSlozka.glob("*.pdf"))) 


