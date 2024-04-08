# start=1
# end=10
# total=0
# for i in range(start,end):
#     if i%2==0:
#         total=total+i
# print(total)


#not opyimal
# def factors1(n):
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i, end=" ")
#     print()

#optimal
def factors2(n):
    for i in range(1, int(n**0.5) + 1):#we used square root i.e n raise to 1/2 is used for sq root 
        if n % i == 0:
            print(i)
            if n // i != i:
                print(n // i)4
    print()


# factors1(3600000000)
factors2(360000000000000)