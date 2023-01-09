a=[10,7,9]
b=[5,23,21]
c=[]
for x,y in zip(a,b):
    c.append(x+y)
print(a,b,c,sep="\n")