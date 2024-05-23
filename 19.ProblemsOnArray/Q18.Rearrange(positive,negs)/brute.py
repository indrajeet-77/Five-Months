def rearrange(arr):
    n=len(arr)
    pos=[]
    neg=[]
    for i in range(n):
        if arr[i]<0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    for i in range(len(pos)):
        arr[i*2]=pos[i]
        arr[i*2+1]=neg[i]
    return arr
x=[2,3,-1,-2]
print(rearrange(x))
