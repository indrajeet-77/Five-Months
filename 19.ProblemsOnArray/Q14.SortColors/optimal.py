# Dutch National Flag
# Tc=O(1)
# Sc=O(1)
# def sortcolorsUsingDutchNationalFlag(arr:list):
#     n=len(arr)
#     low=0
#     mid=0
#     high=n-1
#     while mid<=high:
#         if arr[mid]==0:
#             arr[mid],arr[low]=arr[low],arr[mid]
#             low+=1
#             mid+=1
#         elif arr[mid]==1:
#             mid+=1  
#         else :
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high-=1

# x=[0,1,1,0,1,2,1,2,0,0,0,0]
# print(sortcolorsUsingDutchNationalFlag(x))
# print(x)




def sortColorsUsingDutchNationalFlag(arr:list):
    n=len(arr)
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if  arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
      
x=[1,2,0,1,1,2,1,0]
print(sortColorsUsingDutchNationalFlag(x))
print(x)
                
            
            
    
            
    