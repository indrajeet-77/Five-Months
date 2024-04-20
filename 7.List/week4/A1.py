# Q1. Make a list of your own. Make two more empty list like odd and even.
# Put all the even numbers from original list to even and odd numbers to
# odd and print both lists. (Don’t remove anything from original one).

# my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# even=[]
# odd=[]
# n=len(my_list)
# for i in range(n):
#    if my_list[i]%2==0:
#          even.append(my_list[i])
#    else:
#        odd.append(my_list[i])
# print(my_list)
# print(even)
# print(odd)
    
    
    
    
# 2. Write a function to remove duplicates from a list and print them.
# def removeDuplicates(lst:list):
#     result=[]
#     # n=len(lst)
#     # Method 1
#     '''for i in range(0,n):
#         if lst[i] not in result:
#             result.append(lst[i])
#     return result'''
    
#     # Method 2
#     for i in lst:
#         if i not in result:
#             result.append(i)
#     print(result)

# lst=[1,2,3,2,4,5,4,6,7,6]
# print(removeDuplicates(lst))





# Q3. Write a Python function that takes two lists and returns True if they
# have at least one common element.

# def common(l1,l2)->bool:
#     n=len(l1)
#     m=len(l2)
#     for i in range(n):
#         for j in range(m):
#             if l1[i]==l2[j]:
#              return True
#     return False

# l1=[1,2,3,4]
# l2=[1,5,8,7]
# print(common(l1,l2))





# Q4. Write a Python Program to find sum and average of List in Python.

# from typing import List
# def sum_avg(l1:List[int])->int:
#     n=len(l1)
#     sum=0
#     avg=0
#     for i in range(n):
#         sum+=l1[i]
#     avg=sum/n
#     print(f"Sum = {sum} and avg = {avg}")
# l1=[10,20,30,40] 
# sum_avg(l1)
    
    
    
    
    
#  Q5. Write a program to put all the common elements (in 2 lists) in another
# list and print it using function.   


# def common1(l1,l2)->list:
#     n=len(l1)
#     m=len(l2)
#     l3=[]
#     for i in range(n):
#         for j in range(m):
#             if l1[i]==l2[j]:
#                 l3.append(l1[i])
#     return l3 
# l1=[34,11,91,59,33,22]
# l2=[11,78,14,23,34]
# print(common1(l1,l2))




# Q6. Write a program to remove the nth index element from a list using a
# function.

# def removeNth(l1:list,n:int):
#     l1.pop(n)
#     return l1
# l1=[34,11,91,59,33,22]
# print(removeNth(l1,3))

#without using pop

# def removeNth(l1:list,n:int):
#     if n<0 or n>=len(l1):
#          return l1
#     l2=[]
#     r=len(l1)
#     for i in range(r):
#         if i!=n:
#          l2.append(l1[i])
#     return l2
# l1=[34,11,91,59,33,22]
# print(removeNth(l1,1))






# Q7. Make two lists of same length and pass it to a function. Return a third
# list where each element is the sum of index
# def add(l1,l2):  
#     l3=[]
#     n=len(l1)
#     m=len(l2)
    
#     for i in range(n):
#         for j in range(m):
#          x=l1[i]+l2[j]
#          l3.append(x)
         
#     return l3

# l1=[10,25,30,-10,1,9]
# l2=[58,11,-15,20,6,1]
# print(add(l1,l2))

     
     
     
     
     
# Take 10 integer inputs from user and store them in a list. 
# Now, copy all the elements in another list but in reverse order.

# l=[int(e) for e in input("enter elements:").split(",")]  
# l2=[]
# n=len(l)
# for i in range(n-1,-1,-1):
#     l2.append(l[i])
# print(l2)



# Q9. Make a list. Write a simple program for addition of the 2nd element
# from start and 2nd element from the end.

# l=[int(e) for e in input("Enter elements of list: ").split(",")]
# result=l[1]+l[-2]
# print(result)





# Q10. Ask 10 numbers from the user and put them into the list. Now remove
# all the even numbers from that list.

# l=[int(x) for x in input("Enter 10 numbers : ").split(",")  if int(x)%2 !=0 ]
# print(l)
# Taking list input from user and filtering out elements not divisible by 2





# Q11. Write a python program which prints all the values whose count is
# greater than 3. (Make sure to make a list with at least 15 numbers
# l=[11,22,33,11,11,33,44,55,99,44,11,33,22,22,45,53,22,44]
# l2=[]
# l3=[]
# for i in range(len(l)):
#     x=l.count(l[i])
#     if x>=3:
#         l2.append(l[i])
#         #for i in range(len(l2)): 
#         if l[i] not in l3:
#             l3.append(l2[i])
# print(l3)
    


        

    