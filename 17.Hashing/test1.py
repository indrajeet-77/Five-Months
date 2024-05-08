arr=[2,1,4,5,8,5,8,3,6,7,2,5,5,5]
hash_list=[0]*9
n=len(arr)
#precompute
for i in range(n):
    hash_list[arr[i]]+=1
num=int(input("Enter num: "))
print(hash_list[num])