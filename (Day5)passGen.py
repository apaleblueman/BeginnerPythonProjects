#Password Generator Project
from itertools import repeat
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#inputs
print("Welcome to the PyPassword Generator!")
nol=int(input("Enter number of letters:"))
non=int(input("Enter number of numbers:"))
nos=int(input("Enter number of symbols:"))
#processing
pswd=[]
for l in range(nol):
    pswd+=random.choice(letters)
for n in range(non):
    pswd+=random.choice(symbols)
for s in range(nos):
    pswd+=random.choice(numbers)
np=""
for e in pswd:
    np+=e
print(f"normal pass:{np}")
#print(pswd)
random.shuffle(pswd)
final_pass=""
for d in pswd:
    final_pass+=d

print(f"more secure password is:{final_pass}")