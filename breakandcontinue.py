#continue skips the particular iteration
#break terminates from the loop

for i in range(10):
    if(i%3==0):
        print(i)
    else:
        continue
print("--------------------")
for i in range(10):
    if(i==5):
        break
    else:
        print(i)
