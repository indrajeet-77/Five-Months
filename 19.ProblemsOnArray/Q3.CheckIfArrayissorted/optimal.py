def checkArrayIssorted(arr:list):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
x=[1,2,3,4,5]
print(checkArrayIssorted(x))