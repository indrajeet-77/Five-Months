#largest num in array 1) brute -force code 2)optimal code
#brute force code for largest num in array ,time complexity is O(nlog n)
# def largest(l:list):
#     l.sort()#Time complexity here is O(n log n)
#     return l[-1]
# l=[12,987,567,999,8765,99,12]
# print(largest(l))

#optimal way for largest number in an array , time complexity is O(n)

def largest1(l:list):
    max=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
    return max
l=[12,987,567,999,8765,99,12]
print(largest1(l))


















































#brute force code and timecomplexity is O(nlog n) where n is no of inputs
# def largestnum(l:list):
#    l.sort()# Time complexityo(n)
#    return l[-1]

# x=[838,98,122,199,2,183,0,23,]
# print(largestnum(x))



#optimal code
#so here this is optimal code of largest num in arr and its time complexity is O(n)

# def lagrestnum1(l:list):
#     max=l[0]
#     for i in range(len(l)):
#         if l[i]>max:
#             max=l[i]
#     return max
# x=[838,98,122,199,2,183,0,23,]
# print(lagrestnum1(x))


        