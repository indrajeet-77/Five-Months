# 

def squareroot(x):
    low=1
    high=x
    while low<=high:
        mid=(low+high)//2
        if mid**2==x:
            return  mid
        if mid**2>x:
            high=mid-1
        else:
            low=mid+1
    return high
x=36
print(squareroot(x))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    