def main():
    try:
        a=[10,20,30]
        print(f'Before delete{a}')
        i=int(input('Enter index[0.2]:'))
        x=a.pop(i)
        print(f'{x} deleted from list')
        print(f'After delete:{a}')
    except IndexError:
            print(f'{f} index does not exit')
            print(f'PLease i/p between 0and 2')
        #end :except
main()