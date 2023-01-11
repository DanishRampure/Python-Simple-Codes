#Nested try except
def main():
    try:
        s=input("Enter x:")
        x=int(s)
        s=int(input('Enter y:'))
        y=int(s)
        try:
            z=x/y
            print(f'Quotient:{z}')
        except ZeroDivisionError:
            print(f'Please i/p nonzero for y')
    except ValueError:
        print(f'{s} is invalid number:')
main()