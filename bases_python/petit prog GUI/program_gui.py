from tkinter import *

#======== FENETRE =========

fen = Tk()#création de la fenêtre
fen.title("convert")
fen.geometry("250x160")#taille
fen.config(background = "#054265")

u = IntVar(fen)#valeur

#====================================

text = Label(fen, text = "premier entier :")
text.place(x = 50, y= 0)
text.pack(expand=YES)#permet à rester tjrs au milieu

Entree = Entry(fen)#permet d'insérer une case
Entree.pack(expand=YES)
Entree.place(x = 40, y = 30 )
Entree.pack(expand=YES)

text1 = Label(fen, text = "deuxième entier :")
text1.place(x = 50, y= 60)
text1.pack(expand=YES)

Entree1 = Entry(fen)#permet d'insérer une case
Entree1.pack(expand=YES)
Entree1.place(x = 40, y = 90 )
Entree1.pack()

bouton = Button(fen, text="CALCULER", fg = "green", bg = "#00111A")
bouton.place(x = 60, y = 120)
bouton.pack(expand=YES)

bouton1 = Button(fen, text="quitter", command=fen.destroy, fg = "red", bg = "#00111A")
bouton1.place(x = 180, y = 120)
bouton1.pack(expand=YES)


#========== AFFICHAGE =========

fen.mainloop()