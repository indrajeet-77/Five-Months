# nums=[1,2,3,1]
#       0 1 2 3

# Mycode
# tc=O(log N)
# sc=O(1)
# def peakElement(nums):
#     n=len(nums)
#     low=0
#     high=n-1
#     if n==1:
#         return nums[0]
#     while low<=high:
#         mid=(low+high)//2
#         if nums[mid]>nums[mid-1]and nums[mid]>nums[mid+1]:
#             return mid
#         if nums[mid]<nums[mid-1]:
#             high=mid-1
#         else:
#             low=mid+1
# x=[1,2,3,1]
# print(peakElement(x))


# after learning from sir:
def peakelement(nums):
    n = len(nums)
    low = 0
    high = n - 1
    if n == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    elif nums[n - 1] > nums[n - 2]:
        return n-1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        if nums[mid] > nums[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1


x = [2, 7,10, 8]
print(peakelement(x))
