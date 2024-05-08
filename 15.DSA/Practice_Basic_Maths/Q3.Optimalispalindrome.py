# 3. Leetcode 9 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/
#optimal 
#tc= O(N)
#sc=O(1)

def ispalindrome(x:int)->bool:
    return str(x)==str(x)[::-1]

x=121
print(ispalindrome(x))