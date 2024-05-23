# Tc=O(N**2)
# Sc=o(1 )
def Twosum(arr:list,target):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return [i,j]
arr=[1,2,3,4,5]
target=6
print(Twosum(arr,target))