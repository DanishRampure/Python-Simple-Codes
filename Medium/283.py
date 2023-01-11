def series():
    yield 1
    yield 2
    yield 3
    #raise StopIteration
    #end:series
def main():
    t=series()
    try:
        print(next(t))
        print(next(t))
        print(next(t))
    except StopIteration:
        print('Series ends:')
main()