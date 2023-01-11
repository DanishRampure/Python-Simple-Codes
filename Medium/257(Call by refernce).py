def modify(b):
    b[0]=44;
    b[1]=55;
    b[2]=66
def main():
    a=[10,20,30]
    print(f'Before call:{a}')
    modify(a)
    print(f'After call:{a}')
main()
#Call by reference:
'''Any changes made in user defined fn(modify)
is sent back to calling fn(main)
'''
