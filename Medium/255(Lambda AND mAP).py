def square(v):return v**2
def positive(v2):return v2>0
def main():
    a=[-19,-33,4,-3,23,-3,4,2]
    b=list(map(square,filter(lambda v:v**2,a)))
    print(a,b,sep='\n')
main()
