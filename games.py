import force
import divination

def choose_game():

    print("|--------------------------------------|")
    print("|          CHOOSE YOUR GAME!           |")
    print("|--------------------------------------|")
    print("| (1) Force Game - (2) Divination Game |")
    print("|--------------------------------------|")

    game = int(input("Set the game number: "))

    if(game == 1):
        force.play()
    elif(game == 2):
        divination.play()

if(__name__ == "__main__"):
    choose_game()