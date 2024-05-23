
# This is  not in place 
# def removeduplicates(arr,n):
#     res=[]
#     for i in range(n):
#         if arr[i] not in res:
#             res.append(arr[i])
#     return res
            
# x=[1,2,3,3,4]
# print(removeduplicates(x,5))

# tc=O(N)
# sc=O(1)

def removeduplicates(arr:list):
    if len(arr)==1:
        return 1
    i=0
    j=i+1
    while j<len(arr):
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return arr
x=[1,2,2,3,4,5,6,6]
print(removeduplicates(x))