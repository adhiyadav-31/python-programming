a=10 #global variable
def something():
    a=15
    globals()['a']=20
    print("inside: ",a)

something()

print("outside: ",a)