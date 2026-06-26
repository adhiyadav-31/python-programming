#tuple is a data struucture which is immutable it is one of the 4-built-in data structures in python

tup=(23,45,67,42)
print(type(tup))

print(tup[0])

print(min(tup))

print(max(tup))

print(tup[0])

print(tup.count(23))

print(tup.index(45))

print(len(tup))

tup1=(1,"hello",7.0)

num,word,decimal=tup1

print(num)

print(word)

print(decimal)

tup2=(34,'world',[1,2,3,4])

# **tup2[1]='hello'** #it gives error 
#* is used to show that we cannot modify the elements inside the tuple
#but we can change the elements inside the list which is in tuple
tup2[2][0]=100

print(tup2)

tup3=(20)
print(type(tup3)) #it is not a tuple it is an integer

tup4=(20,)
print(type(tup4)) #it is a tuple of single element