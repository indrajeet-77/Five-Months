# i=0
# while i<=15:
#     print("Hello")
#     i+=1
#use ctrl+c is used to stop infinite output terminAL


# i=1#initialize
# while i<=10:#condition
#     print(i)#code to perform
#     i+=1#increment condition


def pattern(n):
    i=1
    while i>=n:
        print(i,end=" ")
        i+=1
    print()#we used this to  seperate nums till 5 and from 1 to 10 again
pattern(5)
pattern(10)