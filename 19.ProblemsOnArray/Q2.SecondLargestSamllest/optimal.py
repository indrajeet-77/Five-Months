# Problem statement
# You have been given an array ‘a’ of ‘n’ unique non-negative integers.

# Find the second largest and second smallest element from the array.

# Return the two elements (second largest and second smallest) as another array of size 2.

# Example :
# Input: 'n' = 5, 'a' = [1, 2, 3, 4, 5]
# Output: [4, 2]



# using float('inf')
# def second(arr:list):
#     n=len(arr)
#     smallest=float('inf')
#     second_smallest=float('inf')
    
#     largest=float('-inf')
#     second_largest=float('-inf')

#     for i in range(n):
#         if arr[i]<smallest:
#             second_smallest=smallest
#             smallest=arr[i]
#         elif arr[i]<second_smallest and arr[i]!=smallest:
#             second_smallest=arr[i]
#         if arr[i]>largest:
#             second_largest=largest
#             largest=arr[i]
#         elif arr[i]>second_largest and arr[i]!=largest:
#             second_largest=arr[i]
#     return [second_largest,second_smallest]
# x=[1,2,3,4,5,6,7]
# print(second(x))

# tc=o(N)
# sc=o(1)


def secondl(arr:list[int])->list[int]:
    n= len(arr)
    smallest=arr[0]
    sec_small=arr[0]
    
    largest=arr[0]
    sec_largest=arr[0]
    
    for i in range(0,n):
        #largest and second largest 
        
        if arr[i]>largest:
            sec_largest=largest
            largest=arr[i]
        elif arr[i]>sec_largest and arr[i]!=largest:
            sec_largest=arr[i]
            
        # Smallest and second smallest
           
        if arr[i]<smallest:
            sec_small=smallest
            smallest=arr[i]
        elif arr[i]<sec_small and arr[i]!=smallest:
            sec_small=smallest
            
        return [sec_largest,sec_small]
    
x=[1,2,3,4,5,6]
print(secondl(x))
            