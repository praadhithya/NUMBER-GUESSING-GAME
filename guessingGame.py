import random
chances = 0
guess = 0
number = random.randrange(1, 10)
while chances < 5:
    chances = chances + 1
    #print("what is the number ?")
    guess = input("Guess a number ? ")
    if guess == number:
        print("Cangratution YOU WON!!!")
        break
    if not chances < 5:
        print("YOU LOSE!!! the number is",number)