def series():
    yield 1
    yield 2
    yield 3#raise iteration
    '''Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly:
yield is a keyword that is used like return
except the function will return a generator.
generators can only be used once:'''
    #end:series
def main():
    t=series()
    for i in t: #i=next(t)
        print(i)
        #end:for
main()