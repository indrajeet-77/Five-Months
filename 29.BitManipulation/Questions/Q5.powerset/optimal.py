def powerset(nums:list):
    result=[]
    n=len(nums)
    for i in range(0,1<<n):
        ans=[]
        for j in range(0,n):
            if nums[i]&(1<<j)!=0:
                ans.append(nums[j])
        result.append(ans.copy())
x=[1,2,3]
print(powerset(x))