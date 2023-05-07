import string


def crack():
    enter = input("Here are the letters: ")
    enter = enter.lower()
    alp = string.ascii_lowercase
    co = 0
    fva = ""
    sva = 0
    f_list = []
    for q in range(25):
        for m in enter:
            if not m.isalpha():
                fva += m
            for n in alp:
                if m == n:
                    fva += alp[(co + sva) % 25].upper()
                    break
                co += 1
            co = 0
        sva += 1
        f_list.append(fva)
        fva = ""
    print(f_list)


crack()
