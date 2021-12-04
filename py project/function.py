string = input("mot: ")

def reverse_function(string):
    string_reverse = ""
    for letter in range(len(string)-1, -1, -1):
        string_reverse += string[letter]
    return string_reverse

print(reverse_function(string))