# def selectionSort(arr:list):
#     n=len(arr)
#     for i in range(0,n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         arr[i],arr[min_index]=arr[min_index],arr[i]
#     return arr
# x=[99,1,3,455,6,29]
# print(selectionSort(x))


# by myslef
def selsort(arr):
    n=len(arr)
    i=0
    while i<n:
        
       min_index=i
       j=i+1
       while j<n:
        if arr[j]<arr[min_index]:
            min_index=j
            j+=1
    arr[i],arr[min_index]=arr[min_index],arr[i]
    i+=1
          
    return arr
x=[99,1,3,455,6,29]
print(selsort(x))
            