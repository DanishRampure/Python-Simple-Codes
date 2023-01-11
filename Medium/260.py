def square(b):
    for i in range(len(b)):
        b[i]=b[i]**2
def main():
    a=[6,10,8]
    print(a)
    square(a)
    print(a)
main()