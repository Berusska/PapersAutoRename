from pdf2image import convert_from_path
pages = convert_from_path('./s00204-016-1827-3.pdf', 50)#[0]


import io
import os
import PySimpleGUI as sg
import PIL
from PIL import Image
import sys

# GUI #

import glob, sys, fitz

# To get better resolution
zoom_x = 2.0  # horizontal zoom
zoom_y = 2.0  # vertical zoom
mat    = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension


filename = "./s00204-016-1827-3.pdf"  # name of pdf file you want to render
doc = fitz.open(filename)
for page in doc:
    pix = page.get_pixmap(matrix=mat)  # render page to an image
    pix.save("/xyz/abcd/1234.png")  # store image as a PNG

pix = doc[0].get_pixmap(matrix=mat)  # render page to an image
img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)


layout = [

        [sg.Image(img)],
        [sg.Submit(), sg.Cancel()]

]

window = sg.Window('My Program', layout)

button,values = window.read()



#toto ano:
from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("420x590")
canvas = Canvas(root,width=2*210,height=2*295)
canvas.pack()
# pilImage = Image.open("ball.gif")
image = ImageTk.PhotoImage(pages[0])
imagesprite = canvas.create_image(210,295,image=image)
root.mainloop()



#https://stackoverflow.com/questions/18369936/how-to-open-pil-image-in-tkinter-on-canvas
root=Tk()
# image = Image.open("/path/to/your/image.jpg")
canvas=Canvas(root,width=2*210,height=2*295)
basewidth = 150
wpercent = (basewidth / float(pages[0].size[0]))
hsize = int((float(pages[0].size[1]) * float(wpercent)))
image = pages[0].resize((basewidth, hsize), PIL.Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
item4 = canvas.create_image(210,295, image=photo)

canvas.pack(side = TOP, expand=True, fill=BOTH)
root.mainloop()



## CHATGTP
# convert the PIL image to a format that can be displayed in the GUI
pil_image = Image.open("path_to_image_file.png")
sg_image = sg.Image.from_data(pil_image.tobytes(), size=pil_image.size)





import fitz
import PySimpleGUI as sg

# Load the first page of the PDF file
pdf_file = "./s00204-016-1827-3.pdf"
doc = fitz.open(pdf_file)
page = doc.load_page(0)

# Convert the page to an image buffer
pixmap = page.get_pixmap()
img_bytes = pixmap.tobytes()

# Create a SimplePyGUI window and display the image
layout = [[sg.Image(data=img_bytes)]]
window = sg.Window("PDF Viewer", layout)
event, values = window.read()
window.close()









import PySimpleGUI as sg
import fitz

# Load PDF
pdf_path = './s00204-016-1827-3.pdf'
pdf_doc = fitz.open(pdf_path)

# Create SimplePyGUI window
layout = [[sg.Canvas(size=(800, 600), key='-CANVAS-')]]
window = sg.Window('PDF Viewer', layout)

# Zoom factor
zoom_factor = 1.2

# Initial zoom level
zoom_level = 100

# Load first page
page = pdf_doc.load_page(0)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # Check for mouse wheel movement
    if event == '-CANVAS-':
        if values['-CANVAS-'] == (0, -1):  # Mouse wheel down
            # Zoom out
            zoom_level = zoom_level / zoom_factor
        elif values['-CANVAS-'] == (0, 1):  # Mouse wheel up
            # Zoom in
            zoom_level = zoom_level * zoom_factor
        # Update canvas with new zoom level
        new_size = (int(page.MediaBoxSize[0] * zoom_level / 100), int(page.MediaBoxSize[1] * zoom_level / 100))
        pix = page.getPixmap(matrix=fitz.Matrix(zoom_level / 100, zoom_level / 100), alpha=False)
        img_data = pix.getImageData(output='png')
        canvas = window['-CANVAS-'].TKCanvas
        canvas.delete('all')
        photo = sg.PhotoImage(data=img_data)
        canvas.create_image(0, 0, image=photo, anchor='nw')
        window['-CANVAS-'].update()

window.close()