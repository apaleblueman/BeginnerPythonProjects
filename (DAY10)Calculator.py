import click
#defining arithematic functions
#Add
def add(a,b):
    return a + b
#Substract
def sub(a,b):
    return a - b
#Multiply
def mul(a,b):
    return a * b
#divide
def div(a,b):
    return a / b
#A symbol dictionary
sy_dict={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
    }
#input
def calc_start():
        switch=True
        num1= float(input("enter a number:"))
        for s in sy_dict:
            print(s)
        while switch==True:
                op=input("enter the operations:")
                num2=float(input("enter another number:"))
                cfun=sy_dict[op]
                answer=cfun(num1,num2)
                print(f"{num1} {op} {num2} = {answer} ")
                wanna_cont=input(f"type y to continue with {answer} or n for starting over with null value")
                if wanna_cont == "Y" or wanna_cont == "y":
                    num1 = answer
                else:
                    switch = False
                    click.clear()
                    calc_start()
calc_start()    