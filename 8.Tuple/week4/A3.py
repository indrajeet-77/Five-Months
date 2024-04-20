# Q1. Write a Python program to get the 4th element from the last element
# of a tuple


# my_tuple=(10,22,54,98,34,67)
# print(my_tuple[-4])


# Q2. Write a Python program to find repeated items in a tuple.

# def finfrepa(my_tuple):

#  rep=[]
#  n=len(my_tuple)
#  for i in range(n):
#     if my_tuple[i] in my_tuple[i+1:] and my_tuple[i] not in rep:
#         rep.append(my_tuple[i])
#  return rep
 
# my_tuple=(1,2,2,3,4,5,5,6,4,6)
# print(finfrepa(my_tuple))


# def doesexist(e:int,t):
#     t1=tuple(t)
#     # t=(1,2,3,4,5,6,7,8,9,10)
#     # n=len(t)
#     for i in t1:
#         if i==e:
#          print("Yes")    
#          break
#     else:
#         print("No")
# t=[int(i) for i in input("Enter tuple: ").split(",")]
# e=int(input("Enter: "))
# doesexist(e,t)



# Q4. Write a Python program to reverse a tuple.

# def rev(t):
#     # mthod 1
#     # r=t[::-1]
#     # r1=tuple(r)
#     # print(r1)
    
#     #mthd 2
#     l2=[]
#     n=len(t)
#     for i in range(n-1,-1,-1):
#         l2.append(t[i])
#     t1=tuple(l2)
#     return t1
        
# t=[int(i) for i in input("Enter tuple: ").split(",")]
# print(f"reversed tuple is: {rev(t)}")


# Q5. Write a Python program to check if a string has at least one letter and
# one number. If it has at least one letter and one number then print YES else
# print NO.

def checkstr(string):
    for ch in string :
     if ch.isdigit(): #here isdigit cheks the ch is digit or not
        print('yes')
     elif  ch.isalpha():
        print("no")
string=input("enter a string: ")
checkstr(string)