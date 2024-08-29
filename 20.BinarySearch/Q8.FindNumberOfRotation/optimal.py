def numberofrotations(nums):
    n = len(nums)
    index = -1
    low = 0
    high = n - 1
    minimum = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if nums[low] <= nums[high]:
            if nums[low] < minimum:
                minimum = nums[low]
                index = low
        if nums[low] <= nums[mid]:
            # minimum=min(minimum,low)
            if nums[low] < minimum:
                minimum = nums[low]
                index = low
            low = mid + 1
        else:
            if nums[mid] < minimum:
                minimum = nums[mid]
                index = mid
            high = mid - 1
    return index


x = [7, 1, 2, 3, 4, 5, 6]
print(numberofrotations(x))
