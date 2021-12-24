from tkinter import *

fen = Tk()
fen.geometry("600x300")
fen.title('converter Monnaie')

a = IntVar()
b = IntVar()

selection1 = None
selection2 = None

#dec = bitcoin
#bin = euro
#hex = dollard

#system de selection
def update_selection1(operation):
    global selection1
    selection1 = operation
    print(selection1)

def update_selection2(operation):
    global selection2
    selection2 = operation
    print(selection2)

#fonction de calcul
def biteur(user_input):
    return user_input * 45080

#fonction de verification
def calcul():
    user_input = e1.get()
    conversion = (selection1, selection2)
    if selection1[0:-1] == selection2[0:-1]:
        result['text'] = 'resultat '+ str(user_input)

        #bitcoin vers

    elif conversion == ('bit1','eur2') or ('eur1','bit2'):
        result['text'] = 'resultat '+ str(biteur(user_input))

    elif conversion == ('bin1','dec2'):
        result['text'] = 'resultat '+ str(bindec(user_input))

        #hexa vers decimale

    elif conversion == ('dec1','hex2'):
        result['text'] = 'resultat '+ str(dechex(user_input))

    elif conversion == ('hex1','dec2'):
        result['text'] = 'resultat '+ str(hexdec(user_input))

        #hexa vers binaire

    elif conversion == ('bin1','hex2'):
        result['text'] = 'resultat '+ str(binhex(user_input))

    elif conversion == ('hex1','bin2'):
        result['text'] = 'resultat '+ str(hexbin(user_input))

"""
variable a = première colonne
variable b = seconde colonne

indicator = s'enfonce qu'on appui dessus (ne fonctionne pas si il n'est pas un boutton radio)

value = numéro du boutton (si il n'y a pas le indicator alors change de forme)

"""
#interface graphique
Label(fen, text="Saisissez la valeur à convertir").pack(side=TOP)
e1 = Entry(fen)
e1.pack(side=TOP)
result = Label(fen, text='RESULTAT?',bg='#FAEB00',fg='#013B71')
affichage = result.pack()

Fgauche = Frame(fen)
Fgauche.pack(side=LEFT)
Label(Fgauche, text="Base de départ").pack()
bit1 = Radiobutton(Fgauche, text="₿ (BTC)", width = 15,variable=a, value=1,indicatoron=0,command=lambda: update_selection1('bit1')).pack()
eur1= Radiobutton(Fgauche, text="€ (EUR)", width = 15,variable=a, value=2,indicatoron=0,command=lambda: update_selection1('eur1')).pack()
dol1 = Radiobutton(Fgauche, text="$ (US)", width = 15,variable=a, value=3,indicatoron=0,command=lambda: update_selection1('dol1')).pack()
liv1 = Radiobutton(Fgauche, text="£ (GBP)", width = 15,variable=a, value=4,indicatoron=0,command=lambda: update_selection1('liv1')).pack()
yen1 = Radiobutton(Fgauche, text="¥ (JPY)", width = 15,variable=a, value=5,indicatoron=0,command=lambda: update_selection1('yen1')).pack()

Fdroite = Frame(fen)
Fdroite.pack(side=RIGHT)
Label(Fdroite, text="Base d'arrivee").pack()
bit2 = Radiobutton(Fdroite, text="₿ (BTC)", width = 15,variable=b, value=6,indicatoron=0,command=lambda: update_selection2('bit2')).pack()
eur2= Radiobutton(Fdroite, text="€ (EUR)", width = 15,variable=b, value=7,indicatoron=0,command=lambda: update_selection2('eur2')).pack()
dol2 = Radiobutton(Fdroite, text="$ (US)", width = 15,variable=b, value=8,indicatoron=0,command=lambda: update_selection2('dol2')).pack()
liv2 = Radiobutton(Fdroite, text="£ (GBP)", width = 15,variable=b, value=9,indicatoron=0,command=lambda: update_selection2('liv2')).pack()
yen2 = Radiobutton(Fdroite, text="¥ (JPY)", width = 15,variable=b, value=10,indicatoron=0,command=lambda: update_selection1('yen2')).pack()

Fbottom = Frame(fen)
Fbottom.pack(side=BOTTOM)
bouton1 = Button(Fbottom, text="Convertir", command=calcul).pack()
bouton2 = Button(Fbottom, text="EXIT", fg= "red", command= fen.destroy).pack()

fen = mainloop()