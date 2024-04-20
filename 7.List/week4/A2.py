# Q1. Make your own list of numbers. Ask a start and end position from User.
# Print the list from start position to end position using Slicing


# l1=[10,20,30,40,50,60,70]
# s=int(input("Enter start:"))
# e=int(input("Enter end: "))
# res=l1[s:e:]
# print(l1)




# Q2. Make your own list of numbers. Ask a start and end position from User.
# Make another different list which will contain number from start to end
# position. Use slicing logic

# def hehelist(l1:list,s,e)->list:
#     result=l1[s:e+1:]
#     return result
# l1=[int(i) for i in input("Enter elements of list sep by comma: ").split(",")]
# start=int(input("Enter start:"))
# end=int(input("Enter end: "))
# print(hehelist(l1,start,end))




# Q3. Make your own list. Write a Python program that takes an integer as an
# input, and make a new list containing the last n elements of the original
# list. Using slicing logic.

# n=int(input("Enter n: "))
# my_list=[10,5,15,20,19,22,11,87]
# result=my_list[-n ::]
# print(result)





# Q4. Make your own list. Write a Python program that takes an integer as an
# input, and make a new list containing the last n elements of the original list
# but in reverse order. Using slicing logic

# n=int(input("Enter n: "))
# my_list=[10,5,15,20,19,22,11,87]
# result=my_list[-n ::]
# re=result[::-1]
# print(re)





# Q5. Write a python program to interchange first and last elements in a list.

# l1=[1,2,3,4,5,6]
# x=l1[0]
# l1[0]=l1[-1]
# l1[-1]=x
# print(l1)



# Q6. Write a Python code to split a list into two halves using list slicing.
# (Keep the length of list even)

# l=[1,2,3,4,5,6]
# n=len(l)
# x=n//2
# First_half=l[:x]
# Second_half=l[x:]
# print(First_half,Second_half)