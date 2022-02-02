from tkinter import *
from PIL import ImageTk, Image
from random import *

#setting window
fen = Tk()
fen.geometry("500x500")
fen.resizable(width=False, height=False)
fen.title('cryptonium')
fen.iconbitmap('asset/logo.ico')
can = fen.config(background='#09685c')

#font
c = Canvas(fen, bg='gray16', height=200, width=200).pack()
filename = PhotoImage(file='asset/font.png')
background_label = Label(fen, image=filename)
background_label.place(x=0, y=0)

#config window
code = Label(fen, text='CODE', font=('Pixeled', 10), bg='#10BCA5', fg='#404040')
code.place(x=275, y=163)

numbercoin = Label(fen, text='0', font=('Pixeled', 10), bg='#09685c', fg='#0FB59F')
numbercoin.place(x=450, y=10)
coin = Label(fen, text='c', font=('Pixeled', 10), bg='#09685c', fg='#0FB59F')
coin.place(x=467, y=10)

#function

def generate_ore():
    ore = randint(0,1)
    return ore

#pick_btn
import_picture = Image.open('asset/pick.png')
resized = import_picture.resize((100, 93), Image.ANTIALIAS)
new_picture = ImageTk.PhotoImage(resized)
import_picture = ImageTk.PhotoImage(file='asset/pick.png')

img = Button(fen, image=new_picture, bg='#09685c', borderwidth = 0, activebackground='#09685c')
img.place(x=400, y=400)

#exit
fen = mainloop()