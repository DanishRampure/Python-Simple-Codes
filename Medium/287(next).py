def friends():
    for x in ['raj','ravi','amit']:
        yield x
        #end:for
        #raise StopIteration
        #end friends
def main():
    try:
        t=friends()
        print(next(t))
        print(next(t))
        print(next(t))
        print(next(t))
    except StopIteration:
        pass
main()
    