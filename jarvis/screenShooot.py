import pyautogui as pa
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas1 = tk.Canvas(root , width=300, height=300)
canvas1.pack()

def takescreenshot():
    myscreenshot = pa.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_screenshot.png")

myButton = tk.Button(text = "take Screenshot",command=takescreenshot, font=10)
canvas1.create_window(100,100,window=myButton)
root.mainloop()
