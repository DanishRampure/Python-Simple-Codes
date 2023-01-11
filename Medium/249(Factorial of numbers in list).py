def factorial(n):
    f=i=1
    while i<=n-1:
        f=f*i
        i+=1
    return f
def main():
    a=[5,6,7]
    b=[factorial(x) for x in a]
    print(b)
    c=list(map(factorial,a))
    print(c)
main()