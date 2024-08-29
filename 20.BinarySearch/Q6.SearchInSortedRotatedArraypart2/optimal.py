# TC=O(log N)
# Sc=O(1)
# we used binary search here

def SearchInSortedRotated(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low=low+1
            high=high-1
            continue
        if nums[low]<=nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high=mid-1
                
            else:
                low=mid+1
        else:
            if nums[mid]<=target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False
x=[6,7,8,1,2,3,4,5]
t=1
print(SearchInSortedRotated(x,t))