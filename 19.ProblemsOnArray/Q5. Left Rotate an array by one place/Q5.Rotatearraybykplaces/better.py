# tc=O(k)+O(n-k)==O(N)
# sc=O(1)
def rotatearray(arr,k):
    n=len(arr)
    arr[:]=arr[n-k:] + arr[0:n-k]
    return arr
arr=[1,2,3,4,5,6,7]
k=3
print(rotatearray(arr,k))
