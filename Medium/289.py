def square():
    for x in range(10,13): #10  11 12
        yield x**2
        #end:for
        #stopiteration(raise)
        #end:square
def main():
    t=square()
    try:
        print(next(t))
        print(next(t))
        print(next(t))
        print(next(t))
    except StopIteration:
        pass
main()

        