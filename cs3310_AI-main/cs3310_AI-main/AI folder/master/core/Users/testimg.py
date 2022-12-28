from tkinter import *
from tkinter.tix import IMAGETEXT

root = Tk()

root.iconbitmap('C:\Users\kenny\OneDrive\Desktop')

my_img = IMAGETEXT.PhotoImage(Image.open("download.png"))
my_label = Label(image=my_img)
my_label.pack()


root.mainloop()