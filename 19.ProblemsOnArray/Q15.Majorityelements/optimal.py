# Tc=O(n)/ O(2n) 2n for recheckeing
# Sc=O(1)
# Moores Algorithm
def majorityElements(arr:list)->int:
    n=len(arr)
    candidate=arr[0]
    count=1
    c=1
    for i in range(0,n):
        if arr[i]==candidate:
            count+=1
        else:
            count-=1
        
        if count==0:
            candidate=arr[i]
            count=1
    # im just rechecking the array /as per quo its not essential
    for i in range(0,n):
        if arr[i]==candidate:
            c+=1
    if c>n//2:
        return candidate
        
    return -1
   
        
    
x=[2,2,2,1,2,5,5,5,5,5]
print(len(x))
print(majorityElements(x))
