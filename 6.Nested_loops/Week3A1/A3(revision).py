#1
"""
        1 
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1 
"""
# def pattern1(n:int):
#  for i in range(1,n+1):
#     for j in range(1,n-i+1):
#        print(" ",end=" ")
#     for k in range(i,0,-1):
#       print(k,end=" ")
#     print()
# pattern1(5)



#2
""" 


"""
def pattern2(n:int):
    for  i in range(1,n+1):
        for j in range(n-i,0,-1):
            print(" ",end=" ")
        for k in range(n,n-i,-1):
            print(k,end=" ")
        print()
pattern2(5)