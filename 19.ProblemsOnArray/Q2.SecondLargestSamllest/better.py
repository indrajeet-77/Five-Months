def second(arr:list):
    smallest=float('inf')
    largest=float('-inf')
    sec_small=float('inf')
    sec_large=float('-inf')
    n=len(arr)
    #for loop to get largest and smallest
    for i in range(n):
        if arr[i]<smallest:
            smallest=arr[i]
        if arr[i]>largest:
            largest=arr[i]
        
            
        
    