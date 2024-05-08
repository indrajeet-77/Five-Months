# 1. Number of digits
# https://www.naukri.com/code360/problems/number-of-digits_9173

#brute _-force code
# tc= O(log10 N)
# sc= O(1)

def countdigits(x:int)->int:
    count=0
    while x>0:
        count+=1
        x=x//10
    return count
x=1234
print(countdigits(x))
    