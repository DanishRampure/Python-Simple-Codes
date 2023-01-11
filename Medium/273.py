def square():
           global a
           for i in range(len(a)):
               a[i]=a[i]**2
def main():
    global a
    print(a)
    print(a)
    square()
    print(a)
a=[6,10,8]
main()