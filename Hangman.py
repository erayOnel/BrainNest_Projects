def hangman():
    word = input("Enter a word: ").lower()
    fva = len(word) * "_"
    f_list = []
    s_list = []
    co = 0
    over = 6
    print(f"Length of the word is: {len(word)}")
    while True:
        letter = input("Guess a letter:").lower()
        if len(letter) > 1 or not letter.isalpha():
            print("Invalid input")
        else:
            if letter in s_list:
                print("You guessed that letter")
                print(fva)
            else:
                if letter in word:
                    for m in word:
                        if m == letter:
                            f_list.append(co)
                        co += 1
                else:
                    over -= 1
                s_list.append(letter)
                for z in f_list:
                    fva = fva[:z] + letter + fva[z + 1:]
                co = 0
                f_list = []
                print(fva)
                print(f"Attempt(s) left: {over}")
                if over == 0:
                    print("You lost")
                    print(f"The word is {word}")
                    break
                if fva == word:
                    print("You won")
                    print(fva)
                    break
        print(f"Guessed lettters: {s_list}")


hangman()
