import json

"""
Le fichier data/codons_aa.json contient la correspondance entre codons et acides aminés au format JSON.
Les codons qui ne sont pas dans le fichier sont les codons stop.

    Définir la fonction load_dico_codons_aa qui prend en paramètre un fichier au format JSON et retourne la structure de données chargée en mémoire à partir du JSON.

    Définir la fonction codons_stop prenant en paramètre un dictionnaire dont les clés sont les codons et les valeurs les acides aminés correspondants (chaînes de caractères).
    La fonction retournera un tableau contenant l'ensemble des codons stop,
    c'est-à-dire l'ensemble des codons possibles avec les caractères AUGC qui ne sont pas des clés du dictionnaire.

en gros j'ai tout fait
mais je suis bloquer à la derniere partie
c'est à dire le deuxieme definir

"""
def load_dico_codons_aa(chemin):
    fichier = open(chemin,"r")
    strjson = fichier.read()
    fichier.close()
    cours = loads(strjson)
    print(cours)

load_dico_codons_aa("/home/ali/bureau/sae2/data/codons_aa.json")

def codons_stop(dico):