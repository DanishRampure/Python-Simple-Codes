'''Passing multiple value to a function'''
def add(a,b):
    print(f'addition of two numbers is{a+b}')
def multiply(c,d):
    print(f'Multiply is {c*d}')
def main():
    print("enter two numbers:")
    x,y=int(input()),int(input())
    add(x,y)
    multiply(x,y)
main()