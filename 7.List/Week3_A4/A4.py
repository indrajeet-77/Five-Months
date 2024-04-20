# Q1. Make a list of your own. Print the whole list in reverse using FOR loop
# and WHILE loop.
# my_list=[10,20,30,40,50,60,70,80,1000]
# n=len(my_list)
# for i in range(n-1,-1,-1):
#     print(my_list[i],end=" ")

#while loop
# my_list=[10,20,30,40,50,60,70,80,1000]
# n=len(my_list)-1
# while n>-1:
#     print(my_list[n],end=" ")
#     n-=1
    
    
    
    
# Q2. Make a list of your own. Print all the numbers divisible by 3 and 4 in
# that list.
# l1=[10,99,2,4,92,34,11,8,7,30,40,16,12]
# for i in l1:
#     if i%3==0 and i%4==0:
#         print(i,end=" ")




# Q3. Make a list of your own. Count how many numbers are divisible by 5.

# l1=[1,2,3,4,5,10,15,25,55,45,35,44,98,100,115,110]
# count=0
# for i in l1:
#     if i%5==0:
#         count+=1
# print(f"There are {count} numbers are divisible by 5 ",end=" ")




# 4. Make a list of your own. Calculate the length of that list without using
# len() function.

# l1=[11,223,2332,88.4,445.664,66,234,678]
# count=0
# for i in l1:
#     count+=1
# print(count)




# Q5. Create a function countOddEven that accepts an List of Integers and
# print how many even and odd numbers are there.

# def countOddEven(n:list[int]):
#     e_count=0
#     o_count=0
#     for i in n:
#         if i%2==0:
#             e_count+=1
#         else:
#             o_count+=1
#     print(f"Total even numbers= {e_count}")
#     print(f"Total odd numbers= {o_count}")  
# n=[1,2,3,4,5,6,6,7,7,8,8,9,9,10,11]      
# countOddEven(n)




# Q6. Create a function sumCountOddEven that accepts an List of Integers
# and calculate sum of even and odd numbers.

# def sum_of_even_odd(my_list:list):
#     e_sum=0
#     o_sum=0
#     for i in range(len(my_list)):
#         if my_list[i]%2==0:
#             e_sum+=my_list[i]
#         else:
#              o_sum+=my_list[i]
#     print(f"Sum of even numbers ={e_sum}")
#     print(f"Sum of odd numbers= {o_sum}")
      
# my_list=[1,2,3,4,5,6,7,8,9,10]
# sum_of_even_odd(my_list)





# Q7. Create a function findLargest that accepts an List of Integers and
# returns the largest number from the list

# def findLargest(my_list:list):
#     largest=my_list[0]
#     for i in range(len(my_list)):
#        if my_list[i]>largest:
#            largest=my_list[i]
#     return largest
            
        
# my_list=[22,89,999,1,18]
# print(findLargest(my_list))





# Q8. Create a function findSmallest that accepts an List of Integers and
# returns the smallest number from the list

# def findsmallest(my_list:list)->int:
#     smallest=my_list[0]
#     for i in range(len(my_list)):
#        if my_list[i]<smallest:
#            smallest=my_list[i]
#     return smallest
            
        
# my_list=[22,89,999,18,1,17]
# print(findsmallest(my_list))


#9 Create a  function which accepts a list and returns smallest even number
#iteration value 
def sm_evn(my_list: list)->int:
    l2=[]
    for i in my_list:
            if i%2==0:
                l2.append(i)           
    small=l2[0]           
    for i in l2:
        if i< small:
            small=i
    return small
my_list=[9,3,4,5,6,7,8,9,10]
print(sm_evn(my_list))            
            