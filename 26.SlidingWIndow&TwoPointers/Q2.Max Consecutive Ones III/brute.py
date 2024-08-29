# tc=O(N**2)==O(n*n+1/2)
# sc=O(1)
def maxcons(nums, k):
    result = 0
    zeros = 0
    n = len(nums)
    for i in range(0, n):
        for j in range(i, n):
            if nums[j] == 0:
                zeros += 1
            result = max(result, j - i + 1)
            if zeros > k:
                break
    return result


arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
print(maxcons(arr, 2))
