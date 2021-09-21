mylist = []
for i in range(0,20,2):
        mylist.append(i)

print(mylist)

#*************************************************
#Another way of creating called list comprehension
#*************************************************
mylist = [i for i in range(0,200,10)]

print(mylist + mylist)
