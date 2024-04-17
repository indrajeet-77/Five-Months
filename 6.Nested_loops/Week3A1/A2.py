'''
# Q1
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 

'''

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()




'''
Q2

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()




'''
Q3

5 
4 5
3 4 5
2 3 4 5
1 2 3 4 5

'''

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()

"""
Q4

5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 

"""

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()
    
    
    

'''
Q5

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''

# for i in range(5,0,-1):
#     for j in  range(1,i+1):
#         print(j,end=" ")
#     print()




"""
Q6
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

"""

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()





'''
Q7
5 4 3 2 1
4 3 2 1
3 2 1 
2 1 
1

'''

# for i in range(6,0,-1):
#     for j in range(i-1,0,-1):
#         print(j,end=" ") 
#     print()




'''
Q8

1 2 3 4 5
2 3 4 5
3 4 5 
4 5
5

'''

# for i in range(2,7):
#     for j in range(i-1,6):
#         print(j,end=" ")
#     print()
    
    
    
    
"""
Q9

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""
# count=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count+=1
#     print()




"""
Q10

1 2 1 2 1
1 2 1 2
1 2 1
1 2
1

"""

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(2,end=" ")
#         else:
#             print(1,end=" ")
#     print()