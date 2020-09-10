print("|---------------------------------|")
print("| welcome to the divination game! |")
print("|---------------------------------|")

secret_number = 42

kick = int(input("-> enter your number: "))

print("- you typed:", kick)

if(secret_number == kick):
    print("- you're right!")
else:
    print("- you missed...")


print("end game.")