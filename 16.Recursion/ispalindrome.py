
def ispalindrome(s:str,i):
  
    #abccba
    if i>=n//2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    ispalindrome(s,i+1)
s="abccbak"
n=len(s)
print(ispalindrome(s,0))
        
    
