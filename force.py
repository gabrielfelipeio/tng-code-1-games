
def play():

    print("|---------------------------------|")
    print("|    Welcome to the FORCE game!   |")
    print("|---------------------------------|")

    secret_word = "banana"
    correct_letters = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    get_it_right = False

    while(not hanged and not get_it_right):

        kick_letter = input("What's the word ? -> set your kick letter: ")
        kick_letter = kick_letter.strip()

        index = 0
        for letter in secret_word:
            if(kick_letter.upper() == letter.upper()):
                correct_letters[index] = letter
                # print("Did found the letter '{}' in the position '{}', into the secret word!".format(
                #     kick_letter, index))
            index = index + 1

        print(correct_letters)

    print("End game.")


if(__name__ == "__main__"):
    play()
