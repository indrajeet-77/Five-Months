
# Q1
"""
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
"""

# def pattern1(n:int):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(j,end=" ")
#         print()
# n=int(input("Enter the value of n: "))
# pattern1(n)




#Q2

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# def pattern2(n:int):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
# n=int(input("Enter the value of n: "))
# pattern2(n)




# Q3
"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5

"""

# def pattern3(n:int):
#     for i in range(n,0,-1):
#         for j in range(i,n+1,):
#           print(j,end=" ")
#         print()
# n=int(input("Enter the value of n: "))
# pattern3(n)



"""
Q4

5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1

"""

# def pattern4(n:int):
#     for i in range(n,0,-1):
#         for j in range(n,i-1,-1):
#             print(j,end=" ")
#         print()
        
# x=5
# pattern4(5)




#Q5
"""
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
"""
# def pattern5(n:int):
#     for i in range(1,n+1,):
#         for j in range(1,n-i+2):
#             print(j,end=" ")
#         print()
# pattern5(5)





# Q6
"""
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5 
"""
# def pattern6(n:int):
#     for i in range(1,n+1):
#         for j in range(n,i-1,-1):
#             print(j,end=" ")
#         print()   
# pattern6(5)     




#Q7
"""
5 4 3 2 1
4 3 2 1 
3 2 1
2 1 
1
"""
# def pattern7(n:int):
    
#  for i in range(n,0,-1):
#     for j in range(i,0,-1):
#          print(j,end=" ")
#     print()
# pattern7(5)

     
    

#Q8
"""
1 2 3 4 5 
2 3 4 5
3 4 5
4 5
5


"""

# def pattern8(n:int):
#     for i in range(1,n+1):
#         for j in range(i,n+1):
#             print(j,end=" ")
#         print()
# pattern8(5)


        
#9
"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""  
# def pattern9(n:int):
#      count=1
#      for i in range(1,n+1):
#           for j in range(i,0,-1):
#                print(count,end=" ")
#                count+=1
#           print()
# pattern9(5)

#10
"""
1 2 1 2 1
1 2 1 2
1 2 1
1 2
1
"""
# def pattern10(n:int):
#  for i in range(n,0,-1):
#      for j in range(1,i+1):
#           if j%2==0:
#                print(2,end=" ")
#           else:
#                print(1,end=" ")
#      print()
# pattern10(5)
               
      