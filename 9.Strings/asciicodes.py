# char="a"
# print(ord(char))

x=97
print(chr(x))


#Printing no. of digits in string without using .isdigit
# count=0
# char="ashjxbxjvsa*72t1%^7"
# for ch in char:
#     ascii_code=ord(ch)
#     if ascii_code>=48 and ascii_code <=57:
#         #cause ascii code of num is from 48 to 57
#         # 65-90 for capital alpha
#         # 97 -122 for small alpha
#         # 32 for space
#    # if ch.isdigit():
#          count+=1 
# print(count)



char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"
"""
Capital letters = 
Small letters = 
Digits = 
Spaces = 
Symbols = 

"""
cap,small,dig,space,sym=0,0,0,0,0

for ch in char:
    ascii_code=ord(ch)
    if ascii_code>=65 and ascii_code<=90:
        cap+=1
    elif ascii_code>=97 and ascii_code<=122:
         small+=1
    elif ascii_code>=48 and ascii_code <=57:
        dig+=1
    elif ascii_code==32:
          space+=1
    else:
          sym+=1
print(f"Capital letters= {cap} Small Letters ={small} Digits= {dig} Spaces= {space}  Symbols={sym}")




#sir
# char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"
"""
Capital letters = 5
Small letters = 5
Digits = 6
Spaces = 5
Symbols = 17
"""
# cap_letter, small_letter, digits, spaces, symbols = 0, 0, 0, 0, 0
# for ch in char:
#     ascii_code = ord(ch)
#     if ascii_code >= 65 and ascii_code <= 90:
#         cap_letter += 1
#     elif ascii_code >= 97 and ascii_code <= 122:
#         small_letter += 1
#     elif ascii_code >= 48 and ascii_code <= 57:
#         digits += 1
#     elif ascii_code == 32:
#         spaces += 1
#     else:
#         symbols += 1
# print(cap_letter, small_letter, digits, spaces, symbols)



#new method
# char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"
# cap_letter, small_letter, digits, spaces, symbols = 0, 0, 0, 0, 0
# for ch in char:
#     ascii_code = ord(ch)
#     if "A" <= ch <= "Z":
#         cap_letter += 1
#     elif "a" <= ch <= "z":
#         small_letter += 1
#     elif "0" <= ch <= "9":
#         digits += 1
#     elif ascii_code == 32:
#         spaces += 1
#     else:
#         symbols += 1
# print(cap_letter, small_letter, digits, spaces, symbols)