# Tc=O(n**2)
# Sc=O(1)
def majorityElement(nums: list[int]) :
    n=len(nums)
    max_count=0
    count=0
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                count+=1
            max_count=max(max_count,count)
            if max_count>n//2:
                return nums[i]
x=[2,2,1,2,5,2]
print(majorityElement(x))
    
 