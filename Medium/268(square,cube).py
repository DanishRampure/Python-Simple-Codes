def calculate(x):
    return[x**2,x**3]
def main():
    v=int(input('Enter a number:'))
    square,cube=calculate(v)
    print(f'Square:{square}\n'
          f'Cube:{cube}')
main
