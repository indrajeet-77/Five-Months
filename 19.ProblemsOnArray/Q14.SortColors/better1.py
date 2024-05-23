# tc=O(2N)
# sc=O(1)
def sortcolor(arr:list):
    n=len(arr)
    countzero=0
    countone=0
    counttwo=0
    for i in range(0,n):
     if arr[i]==0:
         countzero+=1
     elif arr[i]==1:
         countone+=1
     elif arr[i]==2:
         counttwo+=1
    # print(countzero,countone,counttwo)
    for i in range(0,countzero):
        arr[i]=0
    for i in range(countzero,countzero+countone):
        arr[i]=1
    for i in range(countzero+countone,n):
        arr[i]=2
        
    return arr        
x=[2,0,2,1,1,0]
print(sortcolor(x))









    
        