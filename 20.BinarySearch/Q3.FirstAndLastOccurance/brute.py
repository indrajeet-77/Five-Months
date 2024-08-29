# Tc=o(n)
# sc=O(1)

def countocurrance(nums,x):
    first=-1
    last=-1
    n=len(nums)
    for i in range(0,n):
        if nums[i]==x:
            if first==-1:
                first=i
            last=i
    return [first,last]
x=[1,2,3,3,3,4,5,6]
print(countocurrance(x,3))