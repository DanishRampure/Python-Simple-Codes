def positive(v1):return v1>0
def square(v2):return v2**2
def main():
    l=[10,-40,24,-5,2,34]
    c=list(map(square,filter(positive,l)))
    print(l,c,sep='\n')
main()