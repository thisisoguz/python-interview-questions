# Python Interview Questions

Interview questions that I have been encountering will be shared here regardless of roles, titles and companies.

Any design patterns etc. aren't taken into account answering them since they are meant to be a general insight for the future interviewees.

## Age Classifier

There are two boundaries of age which are 20 and 40 and the ages that fall in such intervals will be named underaged, age, and boomer respectively.

Input method will be called if the input is wanted to be given by the keyboard.

```
age = int(input("Please specify an age: "))
```

The ages of 20 and 40 are the boundaries, however, there are some edge cases that have to be considered further. For instance, the one less than 0 may be one of them.

```
if age <= 0:
	print("There is something wrong about the age. Please double check it!")
elif age >= 0 and age < 20:
	print("The person is underaged.")
elif age >= 20 and age < 40:
	print("The person is young.")
else:
	print("The person is boomer.")
```

## Summing Up The Odd and Even Numbers in An Interval

Interval here will be specified using the values given by the keyboard.

```
ending_num = int(input("Give the end of the interval: "))
```

While looping through, the counter has to sum up the odd and even numbers each other thoroughly.

```
sum_even = 0
sum_odd = 0
```

The even numbers are decided by using modulo operator. By that, the remainder is calculated. Equation a function to 0 using modulo means that the number can be divided by 2, so, it is an even number. Otherwise, it is an odd number.

```
for i in range(1, ending_num + 1):
    if (i%2 == 0):
        sum_even = sum_even + i
    else:
        sum_odd = sum_odd + i
```

The ones below sum the odd and even numbers up respectively and take the average of them further.

```
print("Sum of the evens is ", sum_even)
print("Mean of the sum of the evens is", sum_even/2)
print("Sum of the odds is ", sum_odd)
print("Mean of the sum of the odds is", sum_odd/2)
```

## Guess The Number Game

Module of random is imported to get rid of coding a function that returns a number randomly.

```
import random
```

Beginning and ending of the interval are decided using the values given by the keyboard.

```
a = int(input("You have 5 chances to guess the number.\nBeginning number is "))
b = int(input("Ending number is "))
```

Here the random value that falls into the interval specified by the keyboard is assigned to a variable.

**Why is it b+1?**

Closing parts of the ranges in Python are excluded by default. So, you have to take it account while specifying ranges.

```
random_number = random.randint(a,b+1)
```

The attemps left will be prompted to the screen, so, the guesser will be more careful while guessing. The attemp will be counted in the for loop.

```
attempt = 0
```

Imagine that the guesser has 5 attempts to win the game. The attempt will be incremented by 1 everytime the guesser tries to guess the number. Then, by extracting it from the total amount of guess, that can be defined in the range of the for loop, the attemps left will be calculated. It can be defined using a for loop as following:

```
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
```
