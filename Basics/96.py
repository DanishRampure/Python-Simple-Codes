#Logical Operator
print("Enter 3 nos:")
x,y,z=int(input()),int(input()),int(input())
if x>y and x>z:
    print(f"{x} is greatest")
elif y>x and y>z:
    print(f"{y} is greatest")
else:
    print(f"{z} is greatest")
    