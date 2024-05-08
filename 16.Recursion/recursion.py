# print N to 1 
#Using RECURSION
# def fun(n):
#     if n==0:
#         return 
#     print(n)
#     fun(n-1)

# fun(5)



#basic practice of recursion
#This function will go to infinite loop so python stops it at 993 th time
# def fun():
#     print("Hello")
#     fun()
#     print("Yes")
# fun()


#Print something  N times without using loop  (Without backtracking)
# def fun(n:int):
#     if n<1:
#         return 
#     print(" c and d ")
#     fun(n-1)
# fun(5)

#print 1-N wihout using loops(Without backtracking)

# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1,n)
# func(1,3)


#print N-1 without using loop(without backtracking)
def func(i,):
    if i<1:
        return
    print(i)
    func(i-1)
func(5)