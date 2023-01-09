Rows=2
Colns=2
a=[None]*Rows
for  r  in range(2):
    a[r]=[None]*Colns
print("Enter the elements:")
for r in range(Rows):
    for c in range(Colns):
        a[r][c]=int(input())
s=0
for row in a:
    for x in row:
        s=s+x
print(f'sum:{s}')
    
        