# Tc=O(N)
# Sc=O(1)

#this is the right  rotate an array by k places
# So to left rotate an array just do the step 3 at first and then step1,step2

# def reversearray(arr,l,r):
#     while l<r:
#         arr[l],arr[r]=arr[r],arr[l]
#         l+=1
#         r-=1

# def rotatearraybyKplaces(arr:list,k):
#     n=len(arr)
#     reversearray(arr,n-k,n-1) #step 1: reverse n-k to n-1 places
#     reversearray(arr,0,n-k-1) #step 2: reverse 0 to n-k-1 places(remaining)
#     reversearray(arr,0,n-1)   #step 3: reverse whole array 0 to n-1
#     return arr
# x=[1,2,3,4,5,6,7,8,9,10]
# k=3
# print(rotatearraybyKplaces(x,k))









# Tc=
# Sc=
def  reversearr(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
def rotatearr(arr,k):
    n=len(arr)
    rotation=k%n
    for i in range(rotation):
        reversearr(arr,n-k,n-1)
        reversearr(arr,0,n-k-1)
        reversearr(arr,0,n-1)
    return arr




























    
    
