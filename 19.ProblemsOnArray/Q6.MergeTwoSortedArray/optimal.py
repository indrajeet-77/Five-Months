# tc=O(N+M)
# sc=O(1)
def merge2sortedarr(arr1, arr2):
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i += 1
        else:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j += 1
    while i < len(arr1):
        if len(res) == 0 or res[-1] != arr1[i]:
            res.append(arr1[i])
        i += 1
    while j < len(arr2):
        if len(res) == 0 or res[-1] != arr2[j]:
            res.append(arr2[j])
        j += 1

    return res


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge2sortedarr(arr1, arr2))


    
        
            

