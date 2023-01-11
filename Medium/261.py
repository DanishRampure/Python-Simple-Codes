'''
Nested Function'''
def display():
    def dollar():
        print('$$$')
    dollar()
    print('Raj')
    dollar()
def main():
    display()
main()