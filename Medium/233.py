def square(side):
    area=side**2
    return area
def main():
    s=int(input('Enter side:'))
    a=square(s)
    print(f'Area:{a}')
main()