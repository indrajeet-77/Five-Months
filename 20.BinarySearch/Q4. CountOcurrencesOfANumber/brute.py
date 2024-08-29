# Tc=O(N)
# Sc=O(1)
def count(arr,n,x):
    c=0
    for i in range(0,n):
        if arr[i]==x:
            c+=1
    return c