# 3. Leetcode 9 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/
#Better
# tc=O(log N)
# sc=O(1)

def isPalindrome(x:int)->bool:
    orignal_x=x
    result=0
    while x>0:
        result=(result * 10)+(x%10)
        x=x//10
    return  orignal_x==result

