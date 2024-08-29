
# Tc=(n)
# Sc=O(1)
def finfminimum(nums):
    n=len(nums)
    minimum=float('inf')
    for i in range(n):
        if nums[i]<minimum:
            minimum=nums[i]
    return minimum
x=[7,8,9,10,11,12,13,14,1,2,3,4,5,6]
print(finfminimum(x))