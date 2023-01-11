def main():
    try:
        l=['raj','ravi','amit']
        print(f'Before Del:{l}')
        n=input('Enter name:')
        l.remove(n)
        print(f'After Delete:{l}')
    except ValueError:
        print(f'{n} does not exit')
main()