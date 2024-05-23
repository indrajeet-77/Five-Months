# Insertion _sort

def insertionSort(arr:list):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
x=[77,1,67,99,9,175,2,999,39,1000]
print(insertionSort(x))