def display(* names):
    print('List:')
    for x in names:
        print(x)
def main():
    display('Raj','Amit','Vint')
    display('Marvin','Nitin','Mayank')
    display('Jim')
main()

#Variable length arguments
'''When you dont know how many number of arguments
will be passed by user then you use arguments operator'''