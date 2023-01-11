def myrange(sv,ev):
    while sv<ev:
        yield sv
        sv+=1
        #end:while
        #raise StopIteration
        #end:myrange
def main():
    t=myrange(5,8)
    try:
        while True:
            print(next(t))
            #end:while
    except StopIteration:
        pass
    #end:Except
    #end:for
        #end:main
main()