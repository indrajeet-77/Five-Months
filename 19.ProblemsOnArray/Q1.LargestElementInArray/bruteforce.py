# 1. Largest Element in an Array
# https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
# tc=O(N log N)
# sc=O(1)

def largestele(arr:list):
    arr.sort()
    return arr[-1]
x=[12,99,102,41]
print(largestele(x))