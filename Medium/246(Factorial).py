def factorial(v1):
    f=i=1
    while i<=v1:
        f=f*i
        i+=1
        return f
def main():
    x=int(input('Enter a number:'))
    r=factorial(x)
    print(f"Factorial :{x}")
main()