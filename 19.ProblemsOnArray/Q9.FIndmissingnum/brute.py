def findmissing(arr):
    n=len(arr)
    for i in range(0,n+1):
        if i not in arr:
            return i
x=[0,1,2,4,5]
print(findmissing(x))