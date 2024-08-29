# 3]Tabulization-> Recursion is not involved here it is Bottom to up approach
# here bottom case is decided first
# Tc=O(N)
# SC=O(N)


n=5
dp=[-1]*(n+1)
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
    
print(dp[n])