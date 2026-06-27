#variable is a container that holds data.
a=5
print(a)

b=5
print(b)

print(id(a)) #it gives the address of the variable a
print(id(b)) #it gives the address of the variable b
#here id of a&b is same because both are pointing to the same value 5
name="wukong"
print(name)
name1="goku"
print(name1) 

print(id(name)) #it gives the address of the variable name
print(id(name1)) #it gives the address of the variable name1
#here id of name&name1 is different because they are pointing to different values

#if we have a long value of string we can get the same id for the same value of string by using intern() function
a="my favourite color is pink and blue"
b="my favourite color is pink and blue "
print(id(a)) #it gives the address of the variable a
print(id(b)) #it gives the address of the variable b