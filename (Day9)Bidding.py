import click
print('''
                     _  
 sold!              [|]=========[] sold!
                _____|_____
               |           |sold!
===========================================
    ''')
#######################
bidlist={}
def bidadd(n,a):
    bidlist[n]=a
#######################
def clear():
    click.clear()
#######################
print("welcome to bid machine")
no_more_bidders=False
while no_more_bidders == False:
                print("please eneter details below")
                name=input("name of bidder:")
                bid=int(input("amount to bid:$"))
                bidadd(n=name,a=bid)
                clear()
                re=input("any more bidders?")
                if re=="no":
                    no_more_bidders=True
mlist=[]
for i in bidlist:
      mlist.append(bidlist[i]) 
winam=max(mlist)
wname=""
for n in bidlist:
    if bidlist[n]==winam:
        wname=n

print(f"winner is {wname} with bid of {winam} dollar(s)")        