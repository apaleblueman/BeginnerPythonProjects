#modules
import random
from click import clear
from cdict import celeb_dict
#some vars
ac=""
bc=""
##########################
key_list=[]
for i in celeb_dict:
    key_list.append(i)
###########################
winning=True
###########################
final_score=0
#functions
def random_celeb():
    """asigns random celebs to two variables"""
    global key_a
    global key_b
    key_a=random.choice(key_list)
    key_b=random.choice(key_list)
    global ac
    global bc
    ac=celeb_dict[key_a]
    bc=celeb_dict[key_b]
def one_random_celeb():
    """assigns one random and one winner celeb to two vars.
    meant to be used after random_celeb()"""
    global key_a
    global key_b
    key_b=random.choice(key_list)
    global ac
    global bc
    ac=celeb_dict[key_winner]
    bc=celeb_dict[key_b]

#########################
def whois_winner():
    global winner
    if (key_a > key_b):
        winner="a"  
        global key_winner
        key_winner=key_a
    elif(key_a < key_b):
        winner="b"
        key_winner=key_b
#################
def start():
        global winning
        global ac
        global final_score
        while (winning==True):
            print("WELCOME TO HIGH OR LOW GAME !!!!")
            if final_score==0:
                random_celeb()
            else:
                one_random_celeb()
            # random_celeb()
            if (ac!=bc):
                print(ac)
                print("------vs------")
                print(bc)
            else:
                if final_score==0:
                    random_celeb()
                else:
                    one_random_celeb()
            #
            #print(key_a ,key_b)
            #user input
            guess=input(f"who has more followers? a:{ac} or b:{bc} :")
            whois_winner()
            if guess == winner:
                print("You won!")
                clear()
                final_score+=1
            elif guess!= winner:
                print("you lose")
                print(f"final score is {final_score}")
                global wanna_play_again
                wanna_play_again=input("do u want to play again?'y' or 'n' ")
                if wanna_play_again == "y" or wanna_play_again == "Y":
                    clear()
                    final_score=0
                    winning=True
                elif wanna_play_again == "n" or wanna_play_again == "N":
                    clear()
                    winning=False
                    print("Ok bbye!")
#start
start()