import string


def encryption():
    enter = input("Here are the letters: ")
    key = int(input("Here is the key (0 -25): "))
    cipher = input("(e)Encrypt or (d)decrypt ?: ")
    if not 0 <= key <= 25:
        raise "Key must be between '0' and '25'"
    enter = enter.lower()
    alp = string.ascii_lowercase
    co = 0
    fva = ""
    if cipher == "e":
        for m in enter:
            if not m.isalpha():
                fva += m
            for n in alp:
                if m == n:
                    fva += alp[(co + key) % 25].upper()
                    break
                co += 1
            co = 0
        return fva
    if cipher == "d":
        for m in enter:
            if not m.isalpha():
                fva += m
            for n in alp:
                if m == n:
                    fva += alp[(co - key) % 25].upper()
                    break
                co += 1
            co = 0
        return fva


print(encryption())
# Codes can be reduced for half but seperate them with if as encrypt and decrypt is faster
