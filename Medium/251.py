def greet():print('Hello')
greet=lambda:print('Hello')
def square(v): return v**2
square=lambda v: v**2
def add(v1,v2):return v1+v2
add=lambda v1,v2:v1+v2
def main():
    greet()
    print(square(7))
    print(add(10,20))
main()