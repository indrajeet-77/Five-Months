'''
Q1

        1
      2 1
    3 2 1 
  4 3 2 1
5 4 3 2 1 

'''
# for i in range(1,6):
#     for j in range(1,5-i+1):
#         print(" ",end=" ")
#     for k in range(i,0,-1):
#         print(k,end=" ")
#     print()





'''
Q2
    
        5
      5 4
    5 4 3
  5 4 3 2
5 4 3 2 1

'''

# for i in range(1,6):
#     for j in range(1,5-i+1):
#         print(" ",end=" ")
#     for k in range(5,5-i,-1):
#         print(k,end=" ")
#     print()




"""
Q3

        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5


"""



# for i in range(1, 5 + 1):
#         for j in range(5 - i):
#             print(" ", end=" ")
#         for k in range(2 * i - 1):
#             print(i, end=" ")
#         print()



"""
Q4

        1 
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1

"""

# for i in range(1, 5 + 1):
#         for j in range(5 - i):
#             print(" ", end=" ")
#         for k in range(2 * i - 1):
#             print(i, end=" ")
#         print()
# for i in range(4,0,-1):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print(i,end=" ")
#     print()




"""
Q5}

1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

"""
for i in range(5,0,-1):
    for j in range(i+1,5):
        print(j,end=" ")
    print()