print("Enter two numbers:")
cp,sp=int(input()),int(input())
if cp>sp:
    print(f"Loss of {cp-sp}")
elif cp<sp:
    print(f"Profit of {sp-cp} ")
else:
    print("No Profit No Loss")


