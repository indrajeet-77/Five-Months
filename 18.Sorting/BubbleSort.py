#Bubble Sort

def bubbleSort(arr:list)->list:
    n=len(arr)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
x=[8,99,7,1,77,102,98,999]
print(bubbleSort(x))