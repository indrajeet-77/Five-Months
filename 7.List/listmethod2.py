l1=[1,2,3,4,5,6]
#remove by index
l1.pop()#default last (-1) indx value pop hogi
print(l1)
x=l1.pop(2)#pop also returns the value which is popped so we can store it in a var

print(x)

#remove by value
y=l1.remove(5)#it doesnt returns
print(y)

#delete
del l1[-1]
print(l1)