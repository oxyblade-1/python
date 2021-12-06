password = input("password: ")

def is_valid_password(password):

    """
    créer une fonction de vérification d'un mot de passe

        - 8 caractère
        - 2 nombres
        - 1 Majuscule
        - 1 minuscule

        réponse bouléene

    """
    number = 0
    number_maj = 0
    number_min = 0

    for letter in range(len(password)):
        if password[letter].isnumeric():
            number += 1

        if password[letter].isupper():
            number_maj += 1

        if password[letter].islower():
            number_min += 1

        return number_min >= 1 and number >= 2 and number_maj >= 1 and len(password) >= 8

    else:
        return False

print(is_valid_password(password))