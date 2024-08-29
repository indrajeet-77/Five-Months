# nums=[1,1,0,0,1,0,1,0]


def lessthanequalto(nums, k):
    l = 0
    r = 0
    Sum = 0
    count = 0
    n = len(nums)
    while r < n:
        Sum += nums[r]
        while Sum > k:
            Sum -= nums[l]
            l += 1
        count = count + ((r - l) + 1)
        r += 1
    return count


def Subarraywithsum(nums, k):
    return lessthanequalto(nums, k) - lessthanequalto(nums, k - 1)


x = [1, 0, 1, 0, 1]
k = 2
print(Subarraywithsum(x, k))
