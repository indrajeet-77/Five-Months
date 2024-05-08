# <!-- 2. Leetcode 7 - Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/ -->
#tc= O(log10 N)
#sc= O(1)
def reverse( x: int) -> int:
        reversed_dig=0
        is_neg=False
        if x<0:
            is_neg=True
            x=x*-1
        while x>0:
         ld=x%10
         reversed_dig=(reversed_dig*10)+ld
         x=x//10
        if is_neg:
            reversed_dig=reversed_dig*-1
        if reversed_dig<(-2**31) or reversed_dig>(2**31-1):
            return 0
        
        return reversed_dig
    
x=-8776
print(reverse(x))

        