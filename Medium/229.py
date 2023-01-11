def display(**records):
    print('Record:')
    for k,v in records.items():
        print(f'{k}:{v}')
def main():
    display(company='Yamaha',cost=9000)
    display(name='raj',roll=101,per=90.5)
main()