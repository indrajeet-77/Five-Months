# tc=O(N)
# sc=O(1)

# def movezeros(arr):
#     n=len(arr)
#     i=0
#     j=i+1
#     while i<n:
#         if arr[i]==0:
#             break
#         i+=1
#     while j<n:
#         if arr[j]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             i+=1
#         j+=1
#     return arr
# arr=[1,0,2,3,0,0,4]
# print(movezeros(arr))

def movezeros(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]==0:
         for j in range(i+1,n):
          if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
    return arr
x=[1,0,2,3,0,0,4]
print(movezeros(x))
                    