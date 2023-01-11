def modify(b):
    b.remove(20)
    b.add(22)
def main():
    a={10,20,30,40}
    print(f'{a}:Before call')
    modify(a)
    print(f'After call:{a}')
main()