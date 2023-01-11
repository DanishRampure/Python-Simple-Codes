def greet(msg,prefix,name):
    print(f'{msg} {prefix} {name}')
def main():
    greet('Hello','Mr','Raj')
    greet(name='Amit',msg='Where are you',prefix='Mr')
main()