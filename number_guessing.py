import random

top_of_range = input("Type in the highest number in the range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type in a number greater than zero next time')
        quit()
else:
    print('Please type in a number next time')
    quit()

random_number = random.randint(0, top_of_range)
print("We have picked a number from 0 to", top_of_range)
print(random_number)
guesses = 0
while True:
    guesses +=1
    number_guess = input("Guess the number: ")
    if number_guess.isdigit():
        number_guess = int(number_guess)
    else:
        print("This is not a number.")
        continue
    if number_guess == random_number:
        print("You got it!")
        break
    elif number_guess > random_number:
        print("You were above the number. Try again.")
    else:
        print("You were below the number. Try again.")

print("You got it in", guesses, "guesses!")

    









