import alpha 
def caeser(msg,shift,fun):
    text=""
    for i in msg:
        if i in alpha.alpha:
                    pos=alpha.alpha.index(i)
                    if fun =='decode':
                        npos=pos-shift
                    else:
                        npos=pos+shift
                    ni=alpha.alpha[npos]
                    text+=ni
        else:
            text+=i
    print(f"{fun}d msg is : {text}")
#######################################################
def ff():
    f=input("encode or decode?")
    m=input("msg?")
    s=int(input("shift value?"))
    if s>26:
        s =s % 26
    caeser(msg=m,shift=s,fun=f)
########################################################
def stt():
        st = input("cipher start?(Y/N)")
        if st == "Y" or st == "y":
            ff()
            stt()
        else:
            print("okay bye")
###################################################
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
stt()
