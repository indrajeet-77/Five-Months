# 1. Largest Element in an Array
# https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
# tc=O(n)
# sc=O(1)

# using function max

# def largest(arr:list):
#     n=len(arr)
#     maxi=float('-inf')
#     for i in range(n):
#         maxi=max(maxi,arr[i])
#     return maxi
# x=[1,2,3,4,77,99,10222]
# print(largest(x))


# without using max:
# def largest(arr:list)->int:
#     max=arr[0]
#     n=len(arr)
#     for i in range(n):
#         if arr[i]>max:
#             max=arr[i]
#     return max
# x=[1,98,9,1000]
# print(largest(x))
