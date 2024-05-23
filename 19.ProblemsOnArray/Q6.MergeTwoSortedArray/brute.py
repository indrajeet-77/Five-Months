# sc=O(1)
# tc=O(M+N)

def mergeTwoSortedArrays(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    freq_set=set()#we are using set here cause set only have unique elements
    for i  in range(n):
        freq_set.add(arr1[i])
    for i in range(m):
        freq_set.add(arr2[i])
    return sorted(list(freq_set))
a=[1,2,3,3,4,5,10]
b=[1,2,3,3,6,7,8,9,9]
print(mergeTwoSortedArrays(a,b))
        