"""
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 

"""

# n=5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         print(i,end=" ")
#     print()

"""

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
n=9
for i in range(1,n//2+2):
    for j in range(1,n//2-i+2):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(i,end=" ")
    print()
    
for i in range(n//2,0,-1):
    for j in range(1,n//2-i+2):
        print(" ",end=" ")
    for k in range(1,2*i):
         print(i,end=" ")
    print()
    



"""    



"""


n=9
for i in range(1,n//2+2):
    for j in range(1,n//2-i+2):
        print(" ",end=" ")
    for k in range(1,2*i):
        print(k,end=" ")
    print()
    
for i in range(n//2,0,-1):
    for j in range(1,n//2-i+2):
        print(" ",end=" ")
    for k in range(1,2*i):
         print(k,end=" ")
    print()