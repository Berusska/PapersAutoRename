import PySimpleGUI as sg
import time 
Mylist = [1,2,3,4,5,6,7,8,9]

progressbar = [
    [sg.ProgressBar(len(Mylist), orientation="h", size=(51, 10), key="progressbar")] 
]

outputwin = [
    [sg.Output(size=(78,20))]
]

layout = [
    [sg.Frame('Progress', layout = progressbar)],
    [sg.Frame('Output', layout = outputwin)],
    [sg.Submit('Start', sg.Cancel())]
]

window = sg.Window('Custom Progress Meter', layout, keep_on_top=True) 
progress_bar = window["progressbar"]
while True: 
    event, values = window.read(timeout=10)
    if event == 'Cancel' or event is None:
        break 
    elif event == 'Start':
        for i, item in enumerate(Mylist): 
            print(item) 
            time.sleep(1) 
            progress_bar.UpdateBar(i + 1)
# window.closeO 