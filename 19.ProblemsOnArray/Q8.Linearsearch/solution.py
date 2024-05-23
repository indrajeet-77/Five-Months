# tc=O(N)
# sc=O(1)

def linearsearch(arr,key):
    n=len(arr)
    for i in range(n):
        if arr[i]==key:
            return i #here we are returninng the index 
    return -1

x=[1,2,3,4,99,226,1018]
key=9
print(linearsearch(x,key))