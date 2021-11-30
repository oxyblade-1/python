#reproduit la liste

list = ["salut","bonjour","bonsoir"]
#list.extend(list)


#différence entre append et insert
#append insère à la fin de la liste
#insert à un endroit indiqué de la liste

list.append("aurevoir")
list.insert(1,"coucou")

print(list)

#"remove" supprime la première une valeur d'une liste

list.remove("aurevoir")
print(list)

#"pop" supprimer un élément de la liste

list.pop(0)
print(list)

#"clear" tous les élément de la liste sont supprimer
list.clear()
print(list)
print("ta liste viens d'être supprimer")
