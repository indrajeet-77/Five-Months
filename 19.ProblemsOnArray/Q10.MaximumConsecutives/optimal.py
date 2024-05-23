def maxiconsecutivesOnes(arr:list):
    n=len(arr)
    count=0
    maxi=0
    for i in range(n):
        if arr[i]==1:
            count+=1
        else:
            maxi=max(maxi,count)
            count=0
            
    return max(maxi,count)
x=[1,0,1,1,1,1,0,1]
print(maxiconsecutivesOnes(x))