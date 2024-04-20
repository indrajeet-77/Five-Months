# list=[45,43,'hehe',True,-99.9]
# print(id(list))
# list=[55]
# print(list)

my_list=[1,2,3,4]
my_list[0]=100
my_list[-1]=99
print(my_list)
print(id(my_list))
for i in range (len(my_list)):
    if my_list[i]%2==0:
        my_list[i]=0
    else:
        my_list[i]=1
print(my_list)
    #a[i] is ele and i is pos