def myrange(sv,ev):
    while sv<ev:
        yield sv
        sv+=1
        #end:while
        #raise StopIteration
        #end:myrange
def main():
    t=myrange(5,8)
    for i in t:
        print(i)
    #end:for
        #end:main
main()