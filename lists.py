#list is a collection of items in a particular order.It is mutable and can contain duplicate values.
num_list = [1, 2, 3, 4, 5]
print(num_list)
print(num_list[0]) #it gives 1 as output
print(num_list[4]) #it gives 5 as output
print(num_list[0:3]) #it gives [1, 2, 3] as output and it is called as slicing


names_list=['john','joe']

mixed_list=[1,2.0,'kelly']


#nested list;-a list having collection of lists
nested_list=[num_list,names_list]

#if you dont want multiple list just concatenate
mixed_list=num_list+names_list

num_list.append(44)

num_list.count(2)

num_list.insert(2,99) #it adds value at index 2

num_list.remove(2)

num_list.pop()

del num_list[0]

num_list[0]=100#we can change values at specific index