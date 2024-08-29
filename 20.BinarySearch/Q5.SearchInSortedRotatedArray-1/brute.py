# Tc=O(N)
# Sc=O(1)
# we have used linear search here
def searchinsortedrotated(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1
x=[5,6,7,1,2,3,4]
t=6
print(searchinsortedrotated(x,t))