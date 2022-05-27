import random

a = int(input("You have 5 chances to guess the number.\nBeginning number is "))
b = int(input("Ending number is "))
random_number = random.randint(a,b+1)

attempt = 0

for i in range(1,6):
    number_guessed = int(input("Guess a number in the range you specified: "))
    if (number_guessed>random_number):
        attempt += 1
        print("attempts left: ", 5-attempt)
        if (i >= 5):
            print("You are out of guess.")
            break
        print("Guess a number less than the one you guessed previously.")
    elif (number_guessed<random_number):
        attempt += 1
        print("attempts left: ", 5-attempt)
        if (i>=5):
            print("You are out of guess.")
            break
        print("Guess a number greater than the one you guessed previously.")
    else:
        print("You guessed the number.")
        break
