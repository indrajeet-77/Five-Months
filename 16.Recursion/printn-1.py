
#print N-1 without using loop(without backtracking)
def func(i,):
    if i<1:
        return
    print(i)
    func(i-1)
func(5)



# Sum of first N natural numbers without Loop

# def sumOfNums(n:int):
#     if n==0:
#        return 0
#     return n+sumOfNums(n-1)
# x=10
# print(sumOfNums(x))