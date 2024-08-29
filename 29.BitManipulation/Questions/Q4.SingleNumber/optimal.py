# Tc=O(N)
# Sc=O(1)

def SingleNumber(nums):
    ans=0
    n=len(nums)
    for i in range(0,n):
        ans=ans^nums[i]
    return ans
x=[2,3,3,2,4,5,5]
print(SingleNumber(x))