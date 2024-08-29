# the first step of dp is recursion
# 1] Recursion
# 2]Memoization -> Storing data in dp-> recursion is used here it is Top to bottom approach
# 3]Tabulization-> Recursion is not involved here it is Bottom to up approach
# 4]Tabulization [Space optimization]

# NORMAL RECURSION
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n=5
print(fibonacci(n))

