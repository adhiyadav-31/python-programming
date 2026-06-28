#filter:-if we want our desired output then we will go with the filter

li=[1,2,3,4,5,6,7]

evens=list(filter(lambda n : n%2==0,li))

print(evens)

#map:-if we want to modify the actual content

print(evens)

doubles=list(map(lambda num : num*num,evens))
print(doubles)

#reduce:-it reduces the list
from functools import reduce
sum=reduce(lambda n,m : n+m,doubles)
print(sum)
