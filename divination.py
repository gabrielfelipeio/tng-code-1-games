import random

print("|---------------------------------|")
print("| welcome to the divination game! |")
print("|---------------------------------|")

secret_number = random.randrange(1,101)
total_attempts = 0
points = 1000

print("Levels of play, when (1) is easy, (2) is medium and (3) is hard.")
level = int(input("Set the level: "))

if(level == 1):
    total_attempts = 20
elif(level == 2):
    total_attempts = 10
else:
    total_attempts = 5 

for current_attempts in range(1, total_attempts + 1):
    print("Attempt {} of {} total.".format(current_attempts, total_attempts))
    kick = int(input("Enter a number between 1 and 100: "))
    print("You typed:", kick)

    if(kick < 1 or kick > 100):
        print("You must enter a number between 1 and 100")
        continue

    accept = secret_number == kick
    biggerThan = secret_number < kick
    lessThan = secret_number > kick

    if(accept):
        print("You're right! and did {} points!".format(points))
        break
    else:
        if(biggerThan):
            print("You missed... the kick was bigger than the secret number")    
        elif(lessThan):
            print("You missed... the kick was less than the secret number")    
        loss_points = abs(secret_number - kick)
        points = points - loss_points
    
print("End game.")