def main():
    try:
        s=input('Enter x:')
        x=int(s)
        s=input('Enter y:')
        y=int(s)
        z=x/y
        print(f'Quotient :{z}')
    except ValueError:
        print(f"{s} is invalid number:")
    except ZeroDivisionError:
        print(f"Please i/p nonzero value for y:")
main()