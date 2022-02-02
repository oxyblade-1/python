from tkinter import *

#setting root
root = Tk()
root.geometry("500x200")
root.title("Convertisseur monnaie")

#fonction
def eurdol(valeur_input):
    eur_dol = valeur_input * 1.1363##€ -> $
    return eur_dol

def eurpound(valeur_input):
    eur_pound = valeur_input * 0,8517##€ -> £
    return eur_pound

def poundeur(valeur_input):
    pund_eur = valeur_input * 0,8517##£ -> €
    return pund_eur

def doleur(valeur_input):
    dol_eur = valeur_input * 1.1363##$ -> €
    return dol_eur

def dolpound(valeur_input):
    dol_pound = valeur_input * 1.1363##$ -> £
    return dol_pound

def punddol(valeur_input):
    pound_dol = valeur_input * 1.1363##$ -> €
    return pound_dol

#if valeur_input == valeur_input:
#   affichage['txt'] = "result: " + "valeur_input"


#texte
text = Label(root, text='Saissez la somme à convertir').pack(side=TOP)

#variable
valeur_input = IntVar()
e1 = Entry(root, textvariable=valeur_input).pack(side=TOP)

#Frame
Fgauche = Frame(root)
Fgauche.pack(side=LEFT)
Fdroite = Frame(root)
Fdroite.pack(side=RIGHT)

#affichage
text1 = Label(Fgauche, text='Monnaie de départ').pack()
euro1 = Radiobutton(Fgauche, text='€', width=10, indicatoron=0).pack()
dollard1 = Radiobutton(Fgauche, text='$', width=10, indicatoron=0).pack()
pound1 = Radiobutton(Fgauche, text='£', width=10,indicatoron=0).pack()

text2 = Label(Fdroite, text='Monnaie d\'arrivee').pack()
euro2 = Radiobutton(Fdroite, text='€', width=10, indicatoron=0).pack()
dollard2 = Radiobutton(Fdroite, text='$', width=10,indicatoron=0).pack()
pound2 = Radiobutton(Fdroite, text='£', width=10,indicatoron=0).pack()

#fin programme
btn_exit = Button(root, text='EXIT', fg="red", command=root.destroy).pack(side=BOTTOM)
btn_convert = Button(root, text='convertir').pack(side=BOTTOM)

root.mainloop()