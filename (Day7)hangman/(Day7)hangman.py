#choosing a random word
import random
import hangman_art
import hangman_words
words=["hell","bell","yell"]
chosen_word=random.choice(hangman_words.word_list)
#logo
print(hangman_art.logo)
print("how to play:")
print("A word will be given to you and you will guess it's each letter.You have 6 lives.Each wrong answer costs you a live.")
#diplaying empty list
disp=[]
for i in chosen_word:
    disp+="_"
print(disp)
lives=6
#print(f"answer is:{chosen_word}")
#taking user input 
count=len(chosen_word)
eog=False
while eog==False:
    guess= input("Whats your guess")
#checking user input and inserting correct one in disp list
    if guess in disp:
        print(f"you have already guessed {guess}")
    for n in range(count):
            if chosen_word[n] == guess:
                        disp[n]=guess
    print(disp) 
    if guess not in chosen_word:
        lives-=1
        print(hangman_art.stages[lives])
        print(f"you have {lives} lives left")
        if lives==0:
            print("YOU LOSE")
            eog=True
    if "_" not in disp:
        print("YOU WON")
        eog=True
print(f"Answer was :{chosen_word}")