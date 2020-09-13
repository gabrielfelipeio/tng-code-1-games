print("|---------------------------------|")
print("| welcome to the divination game! |")
print("|---------------------------------|")

secret_number = 42
total_attempts = 3
current_attempts = 1

while(current_attempts <= total_attempts):
    print("Attempt ", current_attempts, " of ", total_attempts, " total.")
    kick = int(input("-> enter your number: "))
    print("- you typed:", kick)
    accept = secret_number == kick
    biggerThan = secret_number < kick
    lessThan = secret_number > kick

    if(accept):
        print("- you're right!")
    else:
        if(biggerThan):
            print("- you missed... the kick was bigger than the secret number")    
        elif(lessThan):
            print("- you missed... the kick was less than the secret number")    
    
    current_attempts = current_attempts + 1
    
print("end game.")