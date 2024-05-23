# to rotate an array we need to learn reverse an array
def reversearray(arr,start,end):
    n=len(arr)
    i=start
    j=end
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
x=[1,2,3,4,5,6,7,8,9,10]
print(reversearray(x,2,4))