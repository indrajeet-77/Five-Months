# 4] This is enhanced version of tabulization cause space is optimized here
# TC=O(N)
# SC=O(N)

n=500
prev1=1
prev2=0


for i in range(2,n+1):
    current=prev1+prev2
    prev2=prev1
    prev1=current
print(prev1)