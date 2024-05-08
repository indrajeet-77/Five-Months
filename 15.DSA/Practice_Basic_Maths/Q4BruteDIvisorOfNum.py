# Problem statement
# Given an integer 'N', your task is to write a program that returns all the divisors of 'N' in ascending order.
# For example:
# 'N' = 5.
# The divisors of 5 are 1, 5.

# TC=O(N)
#SC=O(n)



# def divnums(x: int) -> list[int]:
#     l1 = list()
#     num = 1
#     while num <= x:
#         if x % num == 0:
#             l1.append(num)
#         num += 1  # This should be inside the loop
#     return l1
# x = 6
# print(divnums(x))







#Revision Prctice
#Brute_Force
#TC=O(N) (Cause it will iterate N number of times)
#SC=O(1)


# def Brutedivisors(N:int)->list[int]:
#     result=list()
#     for i in range(1,N+1):
#         if N%i==0:
#             result.append(i)
#     return result
# x=31
# print(Brutedivisors(x))



#Better/Also Optimnal
# TC=O(N/2) which is approx N
# SC=O(1)

# def BetterDivisors(N:int)->list[int]:
#     Result=list()
#     for i in range(1,N//2+1):
#         if N%i==0:
#             Result.append(i)
#     Result.append(N)
#     return Result
# x=99
# print(BetterDivisors(x))




#Optimal: this is optimal only if we dont have to return ressult in ascending order , but we used it here .sort() which makes tc= O(Nlog N) 
# so for this case optimal solution is the better one

# TC=O(N log N)
# SC=O(1)

# def OptimalDivisors(N:int)->list[int]:
#     Result=[]
#     for i in range(1,int(N**0.5)+1):
#         if N%i==0:
#             Result.append(i)
#             if N//i!=i:
#                 Result.append(N//i) # for ex : 4 ka ooppsite hota hai 9  uske liye ye condition
#     Result.sort()
#     return Result
        



        






            
        
        
    
    