print("Enter 2 nos:")
x,y=int(input()),int(input())
while True:
    ch=input("+: Add\n -:Sub\n E:Exit\n Choice:")
    if ch=="+":
        print(f"Add is {x+y}")
    if ch=="-":
        print(f"Sub is {x-y}")
    elif ch in "E":
        break
    else:
        print("Wrong Choice")
print("Program ends")