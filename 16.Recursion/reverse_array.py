# input= n=6 ,arr=[5,7,8,1,6,3]
# op= [3,6,1,8,7,5]
# tc= O(N/2)
# sc=O(N/2)


# def rev_arr(arr,s,e):
#     if  s > e:
#         return
#     arr[s],arr[e] = arr[e],arr[s]
#     rev_arr(arr,s+1,e-1)
    

# x = [int (i) for i in input("Enter elements of array sep by comma: ").split(",")]
# x=[5,7,8,1,6,3]
# n=len(x)
# rev_arr(x, 0, n-1)
# # here i have to print x which is updated internally and i dont need to print rev_array cause it dosnt returns anything 
# print(x)


# # For coding ninja
# def reverseArray(n: int, nums: list[int]) -> list[int]:
#     if  n > len(nums)-n-1:
#         return nums
#     nums[n],nums[len(nums)-n-1] = nums[len(nums)-n-1],nums[n]
#     reverseArray(n+1,nums)
    
# x=[3,6,1,8,7,5]
# reverseArray(0,x)
# print(x)


# input= n=6 ,arr=[5,7,8,1,6,3]
# op= [3,6,1,8,7,5]
# reverse array using recursion


# def rev_arr(arr,s,e):
#     if s>e:
#         return
#     arr[s],arr[e]=arr[e],arr[s]
#     rev_arr(arr,s+1,e-1)

# x=[9,4,2,7,1,8,10]
# n=len(x)
# rev_arr(x,0,n-1)
# print(x)





# def printNtimes(n):
#     if n<1:
#         return
#     print("Coding Ninjas",end=" ")
#     printNtimes(n-1)
    
# printNtimes(3)
























