#cards list
ace=11
cards=[ace,2,3,4,5,6,7,8,9,10,10,10,10]
#functions
#card distribution function
def card_dist(n,name):
    for i in range(n):
            c1=random.choice(cards)
            c2=random.choice(cards)
    name+=[c1,c2]
#blackjack checker function
def isit_blackjack():
    if dealers_cards[0]==ace and dealers_cards[1]==10 or dealers_cards[1]==ace and dealers_cards[0]==10:
        print("Its a blackjack on dealer's side,you lose")
    elif my_cards[0]==ace and my_cards[1]==10 or my_cards[1]==ace and my_cards[0]==10:
        print("Black jack on your side you win!")
def card_dist2(name):
    for c in range(1):
        card=random.choice(cards)
    name+=[card]
#modules
import random
from re import T
#start game
end_game=False
while end_game==False:
            print("Welcome to Terminal blackjack")
            start=input("do you wanna start the game?Y/N")
            if start=='Y' or start=='y':
                my_cards=[]
                card_dist(2,my_cards)
                print("----------------------------------------------------------------------------------------------------------------------------------")
                print(f"your cards are: {my_cards} and your score is {sum(my_cards)}" )
                print("----------------------------------------------------------------------------------------------------------------------------------")
                dealers_cards=[]
                card_dist(2,dealers_cards)
                print(f"Dealers card: {dealers_cards[0]}")
                print("----------------------------------------------------------------------------------------------------------------------------------")
                isit_blackjack()
                if isit_blackjack()== True:
                        end_game=True
                
                if sum(my_cards) >21:
                    ace=1
                    if sum(my_cards)>21:
                        print("you lose")
                        end_game=True
                while end_game==False:
                        wanna_cont=input("do you wanna hit or stand?")
                        if wanna_cont=="hit" :
                            card_dist2(my_cards)
                            print(f"cards:{my_cards} and you score is {sum(my_cards)}")
                            card_dist2(dealers_cards)
                        else:
                            print(f"your cards :{my_cards}  your score:{sum(my_cards)}")
                            print(f"dealer's cards:{dealers_cards} dealer's score:{sum(dealers_cards)}")
                            if sum(my_cards)>21 and ace in my_cards:
                                ace=1
                                print("you lose")
                                end_game=True
                            elif sum(my_cards)>21:
                                print("you lose")
                                end_game=True
                            elif sum(my_cards)==sum(dealers_cards):
                                print("its a draw")
                                end_game=True
                            else:
                                print("you win")
                                end_game=True
            else:
                end_game=True  
            start_again=input("do you wanna play again?")
            if start_again=="y" or start_again=="Y":
                end_game=False
            else:
                end_game=True
