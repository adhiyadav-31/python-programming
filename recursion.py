#recursion is a function call itself 
n=5
fac=1
for i in range(1,n+1):
    fac=fac*i
print(fac)

import sys
from time import sleep
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

# count=1

# def greet():
#     global count
#     count=count+1
#     print("hello ",count)
#     sleep(0.05)
#     greet()

# greet()

#factorial using recursion

def fac(n):
    if(n==1 or n==0):
        return 1
    return n * fac(n-1)
fac(5)