def square(x):
    return x**2
def cube(y):
    return y**3
def main():
    r1=square(10)+cube(5)
    r2=square(cube(2))
    r3=square(cube(2)+3)
    r4=suare(cube(2)+square(3))
    print(r1,r2,r3,r4)
main()