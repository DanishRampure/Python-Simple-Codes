def prime(n):
    i=2
    while i<=n-1:
        if n%i==0:
            return False
        i+=1
    return True
def main():
    a=[5,10,40,23,17]
    b=[x for x in a if prime(x)]
    d=list(range(1,101))
    d=list(filter(prime,d))
    c=list(filter(prime,a))
    print(a,c,d,sep='\n')
main()
