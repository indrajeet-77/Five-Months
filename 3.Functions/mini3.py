# def mini(a:int,b:int,c:int)->int:
#     if a<b and a<c:
#         return a
#     elif b<a and b<c:
#         return b
#     return c
# print(mini(1,2,3))

def mini(a:int,b:int,c:int)->int:
    "this functions returns mini value (to show this when hover over the function)"
    return min(a,b,c)
print(mini(11,22,33))