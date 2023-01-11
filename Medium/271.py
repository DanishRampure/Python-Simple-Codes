'''Local Variables:
    VAriables thst s re create inside function  are called local variables
 
 Local Variables can be used only inside that function in which they are created'''
def square():
    x=int(input('x:'))
    s=x**2
    print(f'square:{s}')
def cube():
    y=int(input('y:'))
    print(f'cube{y**3}')
def main():
    square()
    cube()
main()