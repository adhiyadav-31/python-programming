dict={'arnav': 1,'sahil': 2,'alok': 3}
print(dict)

print(dict['arnav']) #it gives 1 as output

print(dict.get('sahil'))

print(dict.get('rahul','Key not found')) #it gives 'Key not found' as output because rahul is not present in the dictionary

keys={'arnav','sahil','alok'}
values={1,2,3}
dict1=dict(zip(keys,values)) #it combines keys and values to form a dictionary and order is not the same because of set
print(dict1)

dict1.pop('arnav') #it removes the key and value from the dictionary

del dict1['sahil'] #it removes the key and value from the dictionary

programming_languages_and_IDES={'python':['vs code','pycharm'],'java':{'core' :'vs code','spring':'iij'},'c++':['devc++','vs code']}