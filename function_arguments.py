def add(num1=0,num2=0): #default arguments
    return num1+num2

result=add(4,5) 

print(result)

#variable length arguments
def add(num1,*num2): 
    sum=num1
    for i in num2:
        sum+=i
    return sum

result=add(4,5,6,7) 

print(result)

#keyword arguments
def person(name,age):
    print("name:",name)
    print("age:",age)
person(age=18,name='adhi')

def person(name,**kwargs):
    print("name:",name)
    for k,v in kwargs.items():
        print(k,":",v)
person(age=18,name='adhi')