from tkinter import *

fen = Tk()
fen.geometry("200x150")#taille de fenêtre

C = Checkbutton(fen, text = "Case" )#creation d'un boutton

C.place(x= 0, y=10)#positionner la fenêtre /!\
C.config(state = DISABLED)#permet de ne pas interagir avec

fen.mainloop()#affichage