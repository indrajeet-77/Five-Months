# Tc=o(n**2)
# sc=o(1)

def largestSubArrayWithSumK(arr,target):
    n=len(arr)
    maxlength=0
    for i in range(0,n):
        for j in range (i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            if sum==target:
                maxlength=max(maxlength,j-i+1)
    return maxlength
array=[1,2,3,1,1,1,1]
k=int(input("Enter k: "))
print(f"Largest Subarray with Sum K is of Length : {largestSubArrayWithSumK(array,k)}")