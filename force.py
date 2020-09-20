
def play():

    print("|---------------------------------|")
    print("|    Welcome to the FORCE game!   |")
    print("|---------------------------------|")

    secret_word = "banana".upper()
    correct_letters = ["_", "_", "_", "_", "_", "_"]
    wrong_letters = []

    hanged = False
    get_it_right = False
    errors = 0

    while(not hanged and not get_it_right):

        kick_letter = input("What's the word ? -> set your kick letter: ")
        kick_letter = kick_letter.strip().upper()

        if(kick_letter in secret_word):
            print("The letter {} was found!".format(kick_letter))
            index = 0
            for letter in secret_word:
                if(kick_letter.upper() == letter.upper()):
                    correct_letters[index] = letter
                index = index + 1
        else:
            print("The letter {} wasn't found...".format(kick_letter))
            wrong_letters.append(kick_letter)
            errors += 1

        hanged = errors == 6
        get_it_right = "_" not in correct_letters
        print("Secret Word: ", correct_letters)
        print("Wrong Letters: ", wrong_letters)

    if(get_it_right):
        print("You Win!")
    else:
        print("You was Hanged...")

    print("End game.")

if(__name__ == "__main__"):
    play()
