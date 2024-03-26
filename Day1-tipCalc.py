print("Welcome to Tip Calculator.")
bill=int(input("What was the total bill? $"))
tip=int(input("What percentage tip would u like to give?10,12 or 15?"))
people=int(input("How many people to split the bill?"))
tip=bill*(tip/100)
bill=bill+tip
bill=bill/people
rill=round(bill,2)
rill="{:.2f}".format(bill)
print(f"Each person should pay{rill}")
