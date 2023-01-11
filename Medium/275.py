def main():
    try:
        age=int(input("Enter age:"))
        if age<=0:
            raise ValueError   #throw
        #end-if
        print(f'Your age {age} years old')
    except ValueError: #catch
            print(f'{age} is invalid \n'
              f'age cannot be -ve')
        #end of except
main()