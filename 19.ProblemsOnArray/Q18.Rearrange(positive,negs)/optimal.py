def rearrange(arr:list):
    n=len(arr)
    newarr=[0]*n
    positive_index=0
    negative_index=1
    for i in range(n):
        if arr[i]<0:
            newarr[negative_index]=arr[i]
            negative_index+=2
        else:
            newarr[positive_index]=arr[i]
            positive_index+=2
    return newarr
x=[2,3,4,-2,-3,-4]
print(rearrange(x))


