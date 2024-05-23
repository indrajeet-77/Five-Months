# Tc=O(n**3)
# Sc=O(1)

def largestSubArrayWithSumK(arr:list,k)->int:
 n=len(arr)
 target=k
 maxlength=0
 for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum==target:
            maxlength=max(maxlength,j-i+1)
        if sum>target:
            break
 return maxlength

array=[1,2,3,1,1,1,1]
k=int(input("Enter k: "))
print(f"Largest sub array with sum k is of length : {largestSubArrayWithSumK(array,k)}")
