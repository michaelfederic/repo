import random

comp = random.randint(1,1001)
count = 10
def compute(guess,comp):
    if guess == comp:
        print("Correct")
    else:
        a = abs(guess - comp)
        #print("You are",a,"off from my number!") 
        if a > 2 and a <=5:
            print("hot hot, you're burning")
        if a > 5 and a <=10:
            print("hot hot")
        if a > 10 and a <=50:
            print("hotter")
        if a > 50 and a <=100:
            print("cold")
        if a > 100:
            print("way off buddy!")

print("Welcome! This is my Guessing Game!\nYou get 10 chances to guess my number between 1,1000!\nI'll give you a few hints!\nGuess my number: ")
while True:
    count-=1
    try:
        guess = int(input("> "))
    except:
        print("Enter numbers only!")
        break
    if guess == comp:
        print("Correct",comp,"was my number!")
        break
    print("You have",count,"guesses left!")
    if count ==0 and guess != comp:
        print("Sorry you ran out of guesses!")
        print("My number was",comp)
        break
    if guess > comp:
        print("Guess lower!")
        compute(guess,comp)
    if guess < comp:
        compute(guess,comp)
        print("Guess higher!")





    
