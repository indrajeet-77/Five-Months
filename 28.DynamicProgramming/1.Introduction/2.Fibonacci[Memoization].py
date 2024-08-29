
# 2]Memoization -> Storing data in dp-> recursion is used here it is Top to bottom approach
# TC=O(N)
# SC=O(N)+O(N)=> Stackspace +DP
# RECURSION WITH DP
def fibonacci(n,dp):
    if n==0:
        return 0
    elif n==1:
        return 1
    dp[n]=fibonacci(n-1,dp)+fibonacci(n-2,dp)
    if dp[n]!=-1:
        return dp[n]

n=10
dp=[-1]*(n+1) #-> Here [-1,-1,-1,-1,-1,-1] this will be created 
print(fibonacci(n,dp))