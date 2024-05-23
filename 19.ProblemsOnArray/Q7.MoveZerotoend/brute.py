

def movezero(arr):
    n=len(arr)
    temp=[]
    for i in range(n):
        if arr[i]!=0:
            temp.append(arr[i])
    for i in range(len(temp)):
        arr[i]=temp[i]
    
    for i in range(len(temp),n):
        arr[i]=0
    return arr
x=[1,2,0,4,0,6,0,0,0,0,7,8,9]
print(movezero(x))
        
    