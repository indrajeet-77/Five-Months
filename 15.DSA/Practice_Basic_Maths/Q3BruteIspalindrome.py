# 3. Leetcode 9 - Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

# tc=O(log10 N)
# sc=O(1)
#Note i have taken org_x to store the orignal value of x for checking whether result==org_x  and x is changing as loop is running

def ispalin(x:int)->bool:
    org_x=x
    res=0
    while x>0:
     a=x%10
     x=x//10
     res=(res*10)+a
     print("Im x:",x)
    #  print(res)
    if res==org_x:
        return True
    return False

x=121
print(ispalin(x))
    