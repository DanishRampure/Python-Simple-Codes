def modify(a,b,c):
    a=30
    b=80.88
    c='Amit'
def main():
    x,y,z=10,30,'Raj'
    print(f'Before call:{x}{y}{z}')
    modify(x,y,z)
    print(f'After call:{x}{y}{z}')
main()

#Call by Value
Any changes made in user defined function(modify)
is not sent back to calling fn(main)