#somme des nombres de 1 à 5

nombre_defini = [1, 2, 3, 4, 5]
resultat = 0

for number in nombre_defini:
    resultat = resultat + number
    
print(resultat)
#résultat 15

#================== VERSION PLUS COMPLEXE =====================

#somme des nombres défini
number = int(input("nombre à additioner: "))
resultat = 0

liste = []

for chiffre in range(number):
    liste.append(chiffre + 1)

print(liste)

for valeur in liste:
    resultat = resultat + valeur

print(resultat)