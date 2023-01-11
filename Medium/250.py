def factorial(n):
    f=i=1
    while i<=n-1:
        f=f*i
        i+=1
    return f
def prime(n):
    i=2
    while i<=n-1:
        if n%i==0:
            return False
        i+=1
    return True
def main():
        a=[4,6,5,10,7,3]
        print(a)
        b=[factorial(x) for x in a if prime(x)]
        print(b)
        c=list(map(factorial,filter(prime,a)))
main()
