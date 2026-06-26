name="xyz" #it is a string
print(name)
#escape sequences (\ is used to overcome the issue we are facing)
#for example if we want to print hello world people's
print('hello world people\'s')
print(name*10)#it displays name 10 times
print('xyz''abc')#it concatenates to strings but you cannoy do the same with one variable and one string
print(name+'abc')#+ is used when we want to add variable and string
#string as collection of characters
text='abcde' #it has index numbers which starts from 0 and len(text-1)
print(text)
print(text[0])
print(text[5]) #it gives index out of range
print(text[-1]) #it gives the elements in the string in reverse order
print(text[-6]) #it gives the first character of original text string
print(text[3:6]) # it gives 'de'
print(text[0:]) #it gives complete text string

#we cannot change a part of string but we can change total string
print(len(text)) #it gives the length of the string

#\n-newline character
print("hello \nWorld") #hello
                       #world
#you can use another method to display in new line
string="""
hello
world
"""
print(string)
