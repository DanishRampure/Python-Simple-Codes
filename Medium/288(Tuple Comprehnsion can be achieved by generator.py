def main():
    #t=friends()
    t=(x for x in ['ravi','Amit','ravi'])
    #   XTuple Comprehnsion---> Generator
    try:
        print(next(t))
        print(next(t))
        print(next(t))
        print(next(t))
    except StopIteration:
        pass
main()
