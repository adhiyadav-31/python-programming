#if statement 
number=int(input("enter a nnumber"))
if number%2==0:
    print("even")
else:
    print("odd")

#elif:-if one condition is true then it willl exit from the loop
number=int(input("enter the number from 0-5:"))
if(number == 0):
    print("zero")
elif(number == 1):
    print("one")
elif(number == 2):
    print("two")
elif(number == 3):
    print("three")
elif(number == 4):
    print("four")
else:
    print("five")

#nested if:-it checks all the conditions also when one condition is true
number=int(input("enter the number from 0-5:"))
if(number == 0):
    print("zero")
if(number == 1):
    print("one")
if(number == 2):
    print("two")
if(number == 3):
    print("three")
if(number == 4):
    print("four")
else:
    print("five")