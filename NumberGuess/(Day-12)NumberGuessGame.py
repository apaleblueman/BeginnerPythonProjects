#Requiered modules
import random
import click
import logoart
#constants
global answer
#list
nums=[]
for i in range(100):
        nums.append(i+1)
#print(nums)
answer=random.choice(nums)
attempts=0
cont=True
#functions
##guess function
def winorlose(m):
    turn=0
    stoploop=False
    while stoploop == False:
            guess=int(input("What is your guess?:"))
            if guess == answer:
                print("RIGHT,you win!!")
                stoploop=True
            else:
                highorlow(g=guess)
                turn=turn+1
                if turn>=m:
                    stoploop=True
                    print("You ran out of turns !!!")
    qa=input("do u wanna play again?(Y/N):")
    if qa == "Y" or qa == "y":
        global cont
        cont=True 
        print("Alright ,letme clear the screen and start again..")
    elif qa == "N" or qa == "n":
        cont=False
        print("OK bye!")
    else:
        print("put a valid anaswer(now quiting)")
        cont=False
##High low function
def highorlow(g):
    if g>answer:
        print("Guess too high!")
    elif g<answer:
        print("Guess too low..")
######################################intro#####################################################
while cont==True:
       # click.clear()
        print(logoart.logo)
        print("Welcome to guess the number!")
        print("I will choose a number between 1 and 100. You will have to guess it !!")
        mode=input("which mode do u want to play in? 'easy' or 'hard'?(press q to quit):")
        if mode == "easy":
            attempts = 10
            winorlose(m=attempts)
        elif mode == "hard":
            attempts = 5
            winorlose(m=attempts)
        else:
            cont=False