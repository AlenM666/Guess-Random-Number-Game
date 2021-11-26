import random

#random generated number
print("Enter the range of numbers you would like\n ")
user_input1 = int(input('Enter minimum range number: '))
user_input2 = int(input('Enter maximum range numer: '))
x = random.randint(user_input1, user_input2)
print(x)

#player trys to guess the number
player = int(input('Guess the random generated number: '))

guess = 0
#logic for guessed number
while player != x:
    guess += 1
    if player == x - 5 or player == x + 5:
        print("You are close! You missed by five!!")
        player = int(input('Guess the random generated number: '))
    elif player == x - 2 or player == x + 2:
        print("You are close! You missed by two!!")
        player = int(input('Guess the random generated number: '))
    elif player == x - 1 or player == x + 1:
        print("You are close! You missed by one!!")
        player = int(input('Guess the random generated number: '))
    else:
        print("Wrong number try again!!!")
        player = int(input('Guess the random generated number: '))

#if guessed right run this         
if player == x:
    print("\nYou guessed right!! You win!!!")
    print("You got it in", guess, "guesses")
    





