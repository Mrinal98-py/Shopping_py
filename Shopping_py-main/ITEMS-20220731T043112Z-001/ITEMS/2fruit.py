import tkinter as tk
from tkinter import *
root= tk.Tk()

#creating the canvas and the entry box

canvas1 = tk.Canvas(root, width = 825, height = 750, bg='Beige' ,relief='raised')
canvas1.pack()


#puting the background

from PIL import Image, ImageTk
   
img = ImageTk.PhotoImage(Image.open("D:/Py/program XII project/ITEMS/2.png"))  
canvas1.create_image(0, 0,  image=img , anchor= NW)

# creating buttons
photo = PhotoImage(file = r"D:/Py/program XII project/ITEMS/Untitled design (2).png") 
 
apple = tk.Button(image = photo,relief = 'sunken', command=lambda: Click(1))
canvas1.create_window(200, 483, window=apple)

guava = tk.Button(image = photo,relief = 'flat', command=lambda: Click(2))
canvas1.create_window(475, 483, window=guava)

strawberry = tk.Button(image = photo, relief = 'raised', command=lambda: Click(3))
canvas1.create_window(735, 483, window=strawberry)

orange = tk.Button(image = photo, relief = 'groove', command=lambda: Click(4))
canvas1.create_window(200, 715, window=orange)

waterm = tk.Button(image = photo,relief = 'rigde', command=lambda:Click(5) )
canvas1.create_window(475, 715, window=waterm)

promegranate = tk.Button(image = photo,relief = 'raised', command=lambda: Click(6))
canvas1.create_window(735, 715, window=promegranate)



root.mainloop()
