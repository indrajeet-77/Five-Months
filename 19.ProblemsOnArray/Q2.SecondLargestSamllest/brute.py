# tc=O(N+N (2N) +N log N +  )
# sc=O(1)

def second(arr:list):
    set(arr)
    arr.sort()
    list(arr)
    return[ arr[1],arr[-2]]

z=[1,2,3,4,5,6]
print(second(z))
