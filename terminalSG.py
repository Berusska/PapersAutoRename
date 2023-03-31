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

window = sg.Window('Custom Progress Meter', layout) 
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
window.closeO 









#https://stackoverflow.com/questions/66381996/print-output-in-the-gui-screen
import PySimpleGUI as sg

# This is the normal print that comes with simple GUI
sg.Print('Re-routing the stdout', do_not_reroute_stdout=False)

# this is clobbering the print command, and replacing it with sg's Print()
print = sg.Print

# this will now output to the sg display.
print('This is a normal print that has been re-routed.')









import PySimpleGUI as sg
output_area = sg.Output()
layout = [[output_area]]
window = sg.Window('My Window', layout, finalize=True)

# write some text to the output area
print = sg.Print

print('Hello, World!')

# display the window
while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break

# close the window
window.Close()









import PySimpleGUI as sg

# This is the normal print that comes with simple GUI
outputwin = sg.Print('Re-routing the stdout', do_not_reroute_stdout=False)

# # this is clobbering the print command, and replacing it with sg's Print()
# print = sg.Print

# # this will now output to the sg display.
# print('This is a normal print that has been re-routed.')

outputwin = [
    [sg.Output(size=(78,20))]
]

layout = [
    [sg.Frame('Output', layout = [[sg.Output(size=(78,20))]])],
    [sg.Submit('Start', sg.Cancel())]
]

Mylist = [1,2,3,4,5,6,7,8,9]


window = sg.Window('Custom Progress Meter', layout) 
print = sg.Print
while True: 
    event, values = window.read(timeout=10)
    if event == 'Cancel' or event is None:
        break 
    elif event == 'Start':
        for i in Mylist: 
            print(i) 
# window.closeO 



#https://stackoverflow.com/questions/63414794/pysimplegui-output-element-linebreak
#https://shinshin86.hateblo.jp/entry/2021/09/25/092419?utm_source=feed





import PySimpleGUI as sg

layout = [[sg.Button("Print Message")]]
window = sg.Window("Print Example", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Print Message":
        sg.Print("Hello, world!")
        
window.close()