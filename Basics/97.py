x=int(input("Enter bill amount:"))
if x>1 and x<100:
    print("No discount")
elif x>=101 and x<200:
    print("5 % discount ")
else:
    print("10% discount")
