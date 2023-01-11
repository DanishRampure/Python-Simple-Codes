def rectangle(l,b):
    return[l*b,2*(l+b)]
def main():
    l,b=int(input('Enter length:')),int(input('Enter breadth'))
    area,perimeter=rectangle(l,b)
    print(f'Area:{area}\n Perimeter:{perimeter}')
main()