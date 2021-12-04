
string = input("mot de passe:\n")

def true_password(string):
    caracter_pass = 8
    validation = True

#8 caractères + 2 nombres + 1 maj + 1 min
    if string >= caracter_pass:
        print(f"votre mot de passe ne possède que seulement {len(string)} carcatères")

    else:
        print(validation)

print(true_password(string))