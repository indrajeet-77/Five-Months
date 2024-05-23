#

def permutations(nums:list,freq:list):
    n=len(nums)
    if len(ds)==n:
        result.append(ds.copy())
        return result
    for i in range(n):
        if freq[i]==0:
            ds.append(nums[i])
            freq[i]=1
            permutations(nums,freq)
            freq[i]=0
            ds.pop()
ds=[]
result=[] 
x=[1,2,3]
f=[0,0,0]
permutations(x,f)
print(result)
            