import random
guess = 0
def guess(x):
    random_number = random.randint(1, x)
# Used global to acces variable outside of function to try it out. Pretty raaaaaad
    global guess
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if  guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print("Yay, congrats. You have guessed the number {random_number} correctly!")

guess(10)

