# Generate a new user password


print("------------------------------------------------")
import random

chars = "abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
newPassword = []
for x in range(8):
    newPassword.append(random.choice(chars))
    finalPassword = ''.join(map(str, newPassword))
print("\nThis is your new password: ",finalPassword)
new_password = input("Please enter your New Password: ")

#generates a new ticket
import random

chars = "1234567890"
ticketNumber = []
for x in range(4):
    ticketNumber.append(random.choice(chars))
    finalNumber = ''.join(map(str, ticketNumber))
print("\nThis is your Ticket Number: ",finalNumber)
import random
for x in range(0):
    print (random.randint(0,50))
problem= input("Enter ticket number ")


print("------------------------------------------------")

#Mad Libs Generator

color = input("Enter a color: ")
pluralNoun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("roses are", color)
print(pluralNoun + " are blue")
print("I love", celebrity)

print("------------------------------------------------")
#guess the number game
import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("guess the number"))
    if user == number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
    elif user>number:
        print("your guess is too high.")
    elif user<number:
        print("your guess is too low.")
else:
    print(f"Nice Try!, but the number is {number}")


