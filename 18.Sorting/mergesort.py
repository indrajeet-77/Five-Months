"""
Merge Sort
Time Complexity: O(n log n) (Best, Average, Worst)
Space Complexity: O(n)
"""


def merge(left,right):
    merged=[]
    i,j=0,0
    
    # merge the two halves by comparing elements
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
            
    # append remaining elementd from left half(when j is exhausted)
    while i<len(left):
         merged.append(left[i])
         i+=1 
    
    # append remaining elements from right half  (when i is exhausted)
    while j<len(right):
        merged.append(right[j])
        j+=1
    return merged
        
def mergesort(arr:list):
    if len(arr)<=1:
        return arr
    
    # dividing array into two halves
    mid=len(arr)//2
    lefthalf=arr[:mid]
    righthalf=arr[mid:]
    
    # recursively sorting each half
    LH=mergesort(lefthalf)
    RH=mergesort(righthalf)
    
    # merge the sorted halves
    return merge(LH,RH)
        
x=[2,4,5,6,1,99,77,102,14]
print(mergesort(x))
# print(x)            