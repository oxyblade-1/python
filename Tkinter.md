# Documentation TKinter (non officielle)

Tkinter est un module python très utile pour la programmation d'interface graphique.
Sa syntexte reste globalement explicite et permet aux utilisateur d'executer leur code
interprété tout un utilisant du graphique

/!\ Utiliser `ctrl` + `F` pour chercher un élément spécifique !

> Création d'une fenêtre

Dans mon cas j'utilise la variable `root` (racine) qui pour moi
symbolise bien le concept. Si vous voulez la changer veuillez vérifier les modification sur tout votre code !

```py
root = Tk() # créer une fenêtre
root.mainloop() # l'afficher
```

* titre d'une fenêtre
```py
root.title('Name')
```

* Dimensionner une fenêtre
```py
root.geometry("500x500")# fenêtre 500pixels x 500pixels
```

* Garder la forme de la fenêtre
```py
root.resizable(width=False, height=False) 
# désactiver le dimensionnement
# width (largeur)
# height (hauteur)
```

* Ajouter un icon
Pour pouvoir mettre une image en tant que logo je vous conseille
d'utilise ce [convertisseur](https://convertio.co/fr/) afin de pouvoir mettre votre image en format `ico`

```py
root.iconbitmap('FilePath/name.ico')
```

* Fond écrand fenêtre
```py
root.config(background='hexacode')
#configurer le font avec un code hexadécimale
#ou un code coleur red, green, blue, ...
```

> Label (Texte)

Le label permet d'afficher du texte sur la fenêtre
il est d'ailleur possible de le configurer avec différent parramètre.
(Tout les parramètre dans le Label ne sont pas obligatoire, vous pouvez donc en ajouter ou en retirer à l'exeption ici de `root`)

```py
text = Label(root, text="text", font=("FontName", 15), fg="hexacode", bg="hexacode")
text.pack()
#bg: background -> couleur de fond du texte
#fg: fontground -> couleur d'écriture de la police
# le .pack() permet d'affichet le texte
```
/!\ Il est possible de mettre le texte sous format image nous en parlerons juste après !

> option affichage pack()

Comme dit précédemment, le .pack() premet à Tkinter d'afficher ce qui a été créer précédemment c'est avec lui que l'on va placé à un endroit précit un texte ou un n'import quelle objet.
Pour reprendre l'exemple précédent, je vais cette foit si le mettre à Gauche
```py
text = Label(root, text="text", font=("FontName", 15), fg="hexacode", bg="hexacode")
text.pack(side=LEFT)
``` 
Voici les directions utilisé pour le pack:
* LEFT (gauche)
* RIGHT (droite)
* BOTTOM (en bas)
* TOP (en haut)

Il est aussi possible de mettre le même texte au milieu pour cela on utilisera plus le `slide`
mais plus tôt le `expand`(étendre) afin de répartir l'objet sur toute la fenêtre.
```py
text = Label(root, text="text", font=("FontName", 15), fg="hexacode", bg="hexacode")
text.pack(expand=YES)
```
Et enfin si vous voulez placer votre objet à un endroit très précis de la fenêtre, on utilisera plus le `.pack()`
Mais le `.place()` avec une position `x` et une position `y` défini.

```py
text = Label(root, text="text", font=("FontName", 15), fg="hexacode", bg="hexacode")
text.place(x=250, y=350)
#ici je me rend en 250 (x) et 350 (y)
```

> Boutton

Nous les avons beaucoup mentionner depuis le début mais je ne vous est pas dit réellement à quoi il pourraient servir.
Un boutton à la différence d'un Label n'est pas objet passif mis au contraire un objet de détection qui va activer activer une commande défini.
admettons que je veuille entrée l'addition de 2+2 et afficher le résultat sur ma fenêtre.
```py
root = Tk()
root.geometry("200x100")
root.resizable(width=False, height=False)
root.title("addition")

#fonction 2+2
def addition():
	result = 2+2
	label.config(text=f"{result}")

boutton = Button(root, text="Calculer", command=addition)
boutton.pack(expand=YES)
label = Label(root, text="resultat")
label.pack(expand=YES)

root.mainloop()
```
![with_result](https://github.com/oxyblade-1/GenPass/blob/main/doc/calcul_noresult.PNG)

et lorsque l'on click sur le boutton il s'affiche `4`.

![no_result](https://github.com/oxyblade-1/GenPass/blob/main/doc/with_result.PNG)

/!\ important d'importer la librairie `tkinter` !

> Frame

> Entry

> Les Images



