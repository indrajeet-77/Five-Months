# Find factorial of a number with recursion
def fct(n):
    if n<1:
        return True
    else:
     return n*fct(n-1)
x=5
print(fct(x))