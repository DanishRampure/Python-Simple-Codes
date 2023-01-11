def modify(b):
    b['name']='Amit'
    b['roll']=50
    b['per']=80.98
def main():
    a={'name':'raj','roll':101,'per':70.43}
    print(f'Before modify{a}')
    modify(a)
    print(f'After call:{a}')
main()