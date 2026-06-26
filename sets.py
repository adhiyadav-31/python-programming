#set is a collection of values
#set is a collection of unordered unique(one element is stored only once) elements.
set1={1,1,2,3,4,5}
#1 is printed only once and the output is not in inserted order

print(1 in set1)

print(len(set1))

print(type(set1))

set2={} #****it is a dictionary
print(type(set2)) #it is a dictionary

set3=set() #it is a empty set
print(type(set3)) #it is a set

character_set={'alok','kumar','singh'}
print(character_set)

set4 = set('hayato')
print(set4)

set5=set('abcdefmnop')
set6=set('aeiou')
print(set5-set6)# it gives elements which are not in set6 but in set 5

print(set5|set6) #it gives union of both sets

print(set5&set6) #it gives intersection of both sets

print(set5^set6) #it gives elements which are not common in both sets