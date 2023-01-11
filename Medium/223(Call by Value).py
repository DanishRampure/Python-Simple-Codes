#Call by value
'''Passing Parameters/Arguments to Functions(Fn)
'''
def display(x):     #accept
    print(f'Value passed{x}')
def main():
    display(10)
    display(30)
    v=50
    display(v)
    display(v+20)
    display(90.11)
    display('Raj')
main()