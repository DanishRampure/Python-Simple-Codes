def one():
    print('   *')
def three():
    print(' ***')
    one()
def five():
    print('*****')
    three()
def main():
    five()
main()