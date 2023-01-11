def positive(v):
    return v>0
def main():
    l=[10,-40,24,-5,2,34]
    c=[x for x in l if positive(x)]
    print(l,c,sep='\n')
main()