'''#Rule:A parameter can be default
value only when all parameter on RHS
of its have a default values'''
def t1(a=10,b):pass #error
def t1(a=10,b=20,c):pass #error
def t1(a=10,b,c=20):pass #error
def t1(a=10,b):pass #error
def t1(a=10,b=20,c=30):pass 

