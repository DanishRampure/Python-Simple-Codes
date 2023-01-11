def greet(msg='Hi',name='Raj'):
    print(msg,name)
def main():
    greet('Hello','Amit')
    greet('Hello')
    greet()
    #error greet(,'Amit')
    greet(name='Amit')
main()
