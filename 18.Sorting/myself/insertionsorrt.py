def myselfInsertionsort(arr:list):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
x=[5,2,4,6,1]
print(myselfInsertionsort(x))