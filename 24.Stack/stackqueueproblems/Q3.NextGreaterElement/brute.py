# nums=[1,3,2,4]
# ans=[3,4,4,-1]
# def NextGreaterElement(nums):
#     n = len(nums)
#     ans = [-1] * n
#     for i in range(0, n):
#         for j in range(i, n):
#             if nums[j] > nums[i]:
#                 ans[i] = nums[j]
#     return ans


# x = [1, 3, 2, 4]
# print(NextGreaterElement(x))


# nums=[1,3,2,4]
# ans=[3,4,4,-1]
# n=5
#            0 1 2 3 4 5 6 7 8 9 img n=10
# note nums=[1,2,3,4,3|1,2,3,4,3]=2n


def NextGreaterElement(nums):
    n = len(nums)
    stack = []
    ans = [-1] * n
    for i in range(2 * n - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= nums[i % n]:
            stack.pop()
        if i < n and len(stack) > 0:
            ans[i] = stack[-1]

        stack.append(nums[i % n])
    return ans


x = [1, 3, 2, 4]
print(NextGreaterElement(x))
