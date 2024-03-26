import string
alpha=list(string.ascii_lowercase)
alpha+=string.ascii_lowercase
alpha+=" "," "," "," "," "," "," "," "," "
print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')
#encoding
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alpha.index(letter)
        new_position=position + shift_amount
        new_letter=alpha[new_position]
        cipher_text += new_letter
    print(f"encrypted text is :- {cipher_text}")
#decoding
def decrypt(ciphered_text,shift_amount):
    decipher_text=""
    for letter in ciphered_text:
        pos=alpha.index(letter)
        npos=pos - shift_amount
        nletter=alpha[npos]
        decipher_text+=nletter
    print(f"decrypted msg is : {decipher_text}")
#input
ED=input("enter 'encode' or 'decode':")
if ED=='encode':
    shift=int(input("enter the shift"))
    msg=input("msg:")
    encrypt(msg,shift)
elif ED=='decode':
    dshift=int(input("enter the shift"))
    dmsg=input("msg:")
    decrypt(dmsg,dshift)