def myselfbubblesort(arr:list):
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
x=[2,4,1,9,7,8]
print(myselfbubblesort(x))