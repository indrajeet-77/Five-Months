#Tc=O(N)
# Sc=O(1)
# This will rotate array to left by 1 place only
def rotatearr(arr:list):
    n=len(arr)
    first=arr[0]
    for i in range(0,n-1):
        j=i+1
        arr[i]=arr[j]
        j+=1
    arr[-1]=first
    return arr
x=[1,2,3,4,5]
print(rotatearr(x))
    