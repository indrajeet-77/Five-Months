#      0 1 2 3 4 5 6 7 8 9 10
# arr=[1,2,2,3,3,4,4,5,5,6,6]
#   e o e o e o e o e o e
#    Normal pair= Even Odd  index
#    Disturbed pair= Odd Even index
def findsingleElements(nums):
    n = len(nums)
    low = 1
    high = n - 2
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        if nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                high = mid - 1
            else:
                low = mid + 1
        if nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                low = mid + 1
            else:
                high = mid - 1


x = [1, 1, 2, 2, 3, 4, 4, 5, 5]
print(findsingleElements(x))
