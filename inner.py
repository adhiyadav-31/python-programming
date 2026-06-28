 #inner function:-it returns the inner function

def outer():
    print("in outer function ")

    def inner():
        print("in inner function")
    
    return inner

something=outer()
something()
