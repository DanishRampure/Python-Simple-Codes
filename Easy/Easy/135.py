l=[None]*3
print("Enter three numbers")
for r in range(len(l)):
    l[r]=int(input())
s=0
for x in l:
    s=s+x
print(f"Sum :{s}")