# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# tc=O(n)
# sc=O(1)


def maxconsicutiveones(nums, k):
    n = len(nums)
    l = 0
    r = 0
    result = 0
    zeros = 0
    while r < n:
        if nums[r] == 0:
            zeros += 1

        if zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        result = max(result, r - l + 1)
        r += 1
    return result


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(maxconsicutiveones(nums, k))
