print("|---------------------------------|")
print("| welcome to the divination game! |")
print("|---------------------------------|")

secret_number = 42
total_attempts = 3

# while(current_attempts <= total_attempts):
for current_attempts in range(1, total_attempts + 1):
    print("Attempt {} of {} total.".format(current_attempts, total_attempts))
    kick = int(input("-> enter a number between 1 and 100: "))
    print("- you typed:", kick)

    if(kick < 1 or kick > 100):
        print("you must enter a number between 1 and 100")
        continue

    accept = secret_number == kick
    biggerThan = secret_number < kick
    lessThan = secret_number > kick

    if(accept):
        print("- you're right!")
        break
    else:
        if(biggerThan):
            print("- you missed... the kick was bigger than the secret number")    
        elif(lessThan):
            print("- you missed... the kick was less than the secret number")    
    
print("end game.")