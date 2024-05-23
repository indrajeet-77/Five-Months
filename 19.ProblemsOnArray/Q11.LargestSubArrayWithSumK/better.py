# this is better solution for +ve elements and optimal for +ve,-ve elements array
arr=[1,2,1,2,1,1,1,1]
target=6
n=len(arr)
maxlength=0
Sum=0
sum_map=dict()
for i in range(0,n):
    Sum+=arr[i]
    if Sum==target:
        maxlength=i+1
    rem=Sum-target
    if rem in sum_map:
        maxlength=max(maxlength,i-sum_map[rem])
    if Sum not in sum_map:
        sum_map[Sum]=i
print(maxlength)





