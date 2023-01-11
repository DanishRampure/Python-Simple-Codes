def positive(v):
    return v>0
def main():
    l=[10,-40,24,-5,2,34]
    c=list(filter(positive,a))
    print(l,c,sep='\n')
main()
'''
The filter() method filters the given sequence with the help of a
function that tests each element in the sequence to be true or not.
'''