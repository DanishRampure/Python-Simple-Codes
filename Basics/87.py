x=int(input("Enter a number:"))
ch=int(input("1:Square \n 2:Cube\n Enter choice:"))
if ch == 1:
    print(f"Square is {x**2}")
elif ch==2:
    print(f"Cube is {x**3}")
else:
    print("Wrong Choice")

