import random


def play():
    show_begin_message()
    secret_word = load_secret_word()
    correct_letters = inicialize_correct_letters(secret_word)
    print("Secret Word: ", correct_letters)
    wrong_letters = []
    hanged = False
    get_it_right = False
    errors = 0

    while(not hanged and not get_it_right):
        kick_letter = ask_for_kick()

        if(kick_letter in secret_word):
            score_correct_kick(secret_word, kick_letter, correct_letters)
        elif(kick_letter in wrong_letters):
            print("The letter '{}' has already been kicked".format(kick_letter))
        else:
            errors += 1
            wrong_letters.append(kick_letter)
            draw_force(errors, kick_letter)
            

        hanged = errors == 7
        get_it_right = "_" not in correct_letters
        print("Secret Word: ", correct_letters)
        print("Wrong Letters: ", wrong_letters)

    if(get_it_right):
        draw_winner_message()
    else:
        draw_loser_message(secret_word)
    print("End game.")

def draw_force(errors, kick_letter):
    print("The letter '{}' wasn't found.".format(kick_letter))
    print(" _________    ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |       O    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |       O    ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |       O    ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |       O    ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |       O    ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |       O    ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |       O    ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def draw_loser_message(secret_word):
    print("You was Hanged, the correct word was: {}".format(secret_word))
    r"""  _______________       
        / _______________ \     
      //                   \/\  
       |   XXX       XXX   |    
       |                   |    
       \__      XXX      __/    
         |\             /|      
         | I I I I I I I |      
         |  I I I I I I  |      
          \_____________/       
             \_______/"""


def draw_winner_message():
    print("You Win!")
    print("    ___________    ")
    print("   '._==_==_=_.'   ")
    print("   .-\\:      /-.  ")
    print("  | (|:.     |) |  ")
    print("   '-|:.     |-'   ")
    print("     \\::.    /    ")
    print("      '::. .'      ")
    print("        ) (        ")
    print("      _.' '._      ")
    print("     '-------'     ")


def score_correct_kick(secret_word, kick_letter, correct_letters):
    print("The letter '{}' was found!".format(kick_letter))
    index = 0
    for letter in secret_word:
        if(kick_letter.upper() == letter.upper()):
            correct_letters[index] = letter
        index = index + 1


def show_begin_message():
    print("|---------------------------------|")
    print("|    Welcome to the FORCE game!   |")
    print("|---------------------------------|")


def load_secret_word():
    words_file = open("words.txt", "r")
    words_to_raffle = []
    for words_file_line in words_file:
        words_file_line = words_file_line.strip()
        words_to_raffle.append(words_file_line)
    words_file.close()
    raffled_word_index = random.randrange(0, len(words_to_raffle))
    secret_word = words_to_raffle[raffled_word_index].upper()
    return secret_word


def inicialize_correct_letters(secret_word):
    correct_letters = ["_" for letter in secret_word]
    return correct_letters


def ask_for_kick():
    kick_letter = input("Set your kick letter: ")
    kick_letter = kick_letter.strip().upper()
    return kick_letter


if(__name__ == "__main__"):
    play()
