def add(a,b):
    c=a+b
    return c
def main():
    print('Enter 2 nos:')
    x,y=int(input()),int(input())
    z=add(x,y)
    print(f'Add is{z}')
main()