'''
Global variables:[GV]
Variables that are created outside
of all functions are called as global variables
All function of that program can use Gv and can modify
content of GV by specifing following syntax:
global var1,var2.....varN
'''
def india():
    global city
    city ='New Delhi'
def japan():
    global city
    city='Tokyo'
def main():
    global city
    india()
    print(f'Capital of India:{city}')
    japan()
    print(f'Capital of japan:{city}')
city=None
main()

    
