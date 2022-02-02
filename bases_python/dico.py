dico = {
    "pseudo" : "oxyblade"
}

dico["poid"] = "60.5kg"#syntaxe incrémenter une variable dans le dictionnaire
dico["name"] = "***"
dico["age"] = 17
dico["game"] = "minecraft"

print(dico)

print("suppresion de la variable game",dico.pop("game"))
#vérifie si la variable game est dans le dictionnaire
print("game" in dico)
#renvoi "False" car elle supprimer

print(dico)

