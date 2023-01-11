def add(v1,v2): return v1+v2
def main():
    a,b=[10,20,30],[7,8,9]
    c=list(map(lambda v1,v2:v1+v2,a,b))
    print(a,b,c,sep='\n')
main()
