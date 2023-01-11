def square(side):
    area=side**2
    print(f'Area:{area}')
def main():
    print("Enter a side of square:")
    side=int(input())
    square(side)
main()