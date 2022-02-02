from tkinter import *

fen=Tk()#création fenêtre
fen.title("fenêtre")
fen.geometry('200x300')

#valeur globale de selection
selection = None

def get_input():
    a=int(e1.get())
    b=int(e2.get())
    return (a, b)

def update_selection(operation):
    global selection
    selection = operation

#permet d'accepter les paramètre d'une fonction pour tkinter
lambda: get_input

#fonction de verification
def calcul():
    if selection == 'addition':
        print(type(get_input()))
        affichage['text']= 'le resultat : '+str(get_input()[0] + get_input()[1])
    
    elif selection == 'soustraction':
        print(type(get_input()))
        affichage['text']= 'le resultat : '+str(get_input()[0] - get_input()[1])

    elif selection == 'multiplication':
        print(type(get_input()))
        affichage['text']= 'le resultat : '+str(get_input()[0] * get_input()[1])

    elif selection == 'division':
        print(type(get_input()))
        affichage['text']= 'le resultat : '+str(get_input()[0] / get_input()[1])

entier1 = Label(fen, text = 'premier entier :')#creation du texte
entier1.pack()#affichage du texte
e1=Entry(fen)
e1.pack()

entier2 = Label(fen, text = 'deuxième entier :')#Réponse6
e2=Entry(fen)
entier2.pack()
e2.pack()

affichage=Label(fen, text='RESULTAT?')
affichage.pack()

choix_calcul=Label(fen, text='type équation')
choix_calcul.pack()

Bcalcul=Button(fen, text="addition", width = 15,command=lambda: update_selection('addition'))
Bcalcul.pack()

Bcalcul=Button(fen, text="soustraction",width = 15,command=lambda: update_selection('soustraction'))
Bcalcul.pack()

Bcalcul=Button(fen, text="multiplication",width = 15,command=lambda: update_selection('multiplication'))#width = taille du boutton en partant du milieu
Bcalcul.pack()

Bcalcul=Button(fen, text="division",width = 15,command=lambda: update_selection('division'))
Bcalcul.pack()

Bcalcul=Button(fen, text="EXIT",command=fen.destroy,fg ="red") #inversion du sen avec la side= BOTTOM
Bcalcul.pack(side=BOTTOM)

Bcalcul=Button(fen, text="calculer",command= calcul)
Bcalcul.pack(side=BOTTOM)

fen.mainloop()