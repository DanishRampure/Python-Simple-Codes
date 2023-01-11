def main():
    try:
        x=int(input('Enter a value of x:'))
        y=int(input('Enter a value of y:'))
        z=x//y
        print(f"Division is {z}")
    
    except ZeroDivisionError:
        print(f'Division by zero not allowed')
        print('Please i/p nonzero value for y')
main()
