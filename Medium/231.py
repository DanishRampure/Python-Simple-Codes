def display(p1,p2,p3):
    print(p1,p2,p3)
def main():
    d1={'p1':10,'p2':20,'p3':30}
    display(**d1)
    d2={'p3':30,'p1':10,'p2':20}
    display(**d2)
    d3={'p1':10,'p2':20}
    #display(**3)#error
    d4={'p1':10,'p2':20,'p3':30}
    display(**d4)
main()