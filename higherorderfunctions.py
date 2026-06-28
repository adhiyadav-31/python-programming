#higher order function:-if we are able to pass one function to another function then it is called higher order function
def square(num):
    return num*num
def cube(num):
    return num*num*num
def operate(num,operation):
    return operation(num)
print(operate(5,square))