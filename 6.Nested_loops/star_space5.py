"""
* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(i,5):
#         print("*",end=" ")
#     print()

#for odd no. of rows
#  if we wanr even +1 krdo first for may

n=6
if n%2==0:
    add=1
else:
    add=2
for i in range(1,n//2+add):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
for i in range(n//2,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()