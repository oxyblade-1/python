from tkinter import *

fen = Tk()
fen.geometry("600x200")
fen.title('converter Multi-bases')

a = IntVar()
b = IntVar()

selection1 = None
selection2 = None

#system de selection
def update_selection1(operation):
    global selection1
    selection1 = operation
    print(selection1)

def update_selection2(operation):
    global selection2
    selection2 = operation
    print(selection2)

#binaire vers decimale
def decbin(user_input):
    return bin(user_input)[2:]

def bindec(user_input):
    return int(str(user_input),2)

#binaire vers hexadecimale
def binhex(user_input):
    return dechex(bindec(user_input))

def hexbin(user_input):
    return decbin(hexdec(user_input))

#hexadecimale vers decimale
def hexdec(user_input):
    return int(str(user_input),16)

def dechex(user_input):
    return hex(user_input)[2:]


#fonction de verification
def calcul():
    user_input = e1.get()
    conversion = (selection1, selection2)
    if selection1[0:-1] == selection2[0:-1]:
        result['text'] = 'resultat '+ str(user_input)

        #binaire vers decimale

    elif conversion == ('dec1','bin2'):
        result['text'] = 'resultat '+ str(decbin(user_input))

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
result = Label(fen, text='RESULTAT?')
affichage = result.pack()

Fgauche = Frame(fen)
Fgauche.pack(side=LEFT)
Label(Fgauche, text="Base de départ").pack()
deci_1 = Radiobutton(Fgauche, text="Decimal", width = 15,variable=a, value=1,indicatoron=0,command=lambda: update_selection1('dec1')).pack()
bin_1 = Radiobutton(Fgauche, text="Binaire", width = 15,variable=a, value=2,indicatoron=0,command=lambda: update_selection1('bin1')).pack()
hexa_1 = Radiobutton(Fgauche, text="Hexadecimal", width = 15,variable=a, value=3,indicatoron=0,command=lambda: update_selection1('hex1')).pack()

Fdroite = Frame(fen)
Fdroite.pack(side=RIGHT)
Label(Fdroite, text="Base d'arrivee").pack()
deci_2 = Radiobutton(Fdroite, text="Decimal", width = 15,variable=b, value=4,indicatoron=0,command=lambda: update_selection2('dec2')).pack()
bin_2= Radiobutton(Fdroite, text="Binaire", width = 15,variable=b, value=5,indicatoron=0,command=lambda: update_selection2('bin2')).pack()
hexa_2 = Radiobutton(Fdroite, text="Hexadecimal", width = 15,variable=b, value=6,indicatoron=0,command=lambda: update_selection2('hex2')).pack()

Fbottom = Frame(fen)
Fbottom.pack(side=BOTTOM)
bouton1 = Button(Fbottom, text="Convertir", command=calcul).pack()
bouton2 = Button(Fbottom, text="EXIT", fg= "red", command= fen.destroy).pack()

fen = mainloop()