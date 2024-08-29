import math

# tc=O(n)+O(log N*N)
# sc=O(1)


def mindiv(nums, threshold, div):
    totalofarray = 0
    for i in range(len(nums)):
        totalofarray += math.ceil(nums[i] / div)
    return totalofarray <= threshold


def minimumdivior(nums, threshold):
    ans = 0
    low = 1
    high = max(nums)
    while low < high:
        mid = (low + high) // 2
        th = mindiv(nums, threshold, mid)
        if th:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


x = [1, 2, 5, 9]
t = 6
print(minimumdivior(x, t))
