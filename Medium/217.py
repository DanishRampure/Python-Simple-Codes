def one():
    print('   *')
def three():
    one()
    print(' ***')
def five():
    three()
    print('*****')
def main():
    five()
main()