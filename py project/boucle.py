#permet de lire une suite quelconque

races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

#====================================
#détecteur du nombre de passager

passager_number  = 10
for passager in range(passager_number):
    #passager (variable du nombre de tour de boucle) à noter qu'elle commence par 0 

    if passager + 1 == 1:
        print(f"bienvenue au {passager + 1}er passager")

    elif passager + 1 == 2:
        print(f"bienvenue au {passager + 1}nd passagers")

    else:
        print(f"bienvenue au {passager + 1}e passagers")

#======================================
