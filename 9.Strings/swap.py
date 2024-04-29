string = "AHKJyfkhKHDWAKJ43298789$&#(*$&dwada  DaD)"
# cap to small small to cap
result=""
for ch in string:
    asci_1=ord(ch)
    if asci_1>=65 and asci_1<=90:
        asci_1+=32
        new1=chr(asci_1)
        result+=new1
    elif asci_1 >=97 and asci_1<=122:
        asci_1-=32
        new1=chr(asci_1)
        result+=new1
    else:
        result+=ch
        
print(result)
    
   #sir 
string = "AHKJyfkhKHDWAKJ43298789$&#(*$&dwada  DaD)"

# def swapcase(string):
#     result = ""
#     for ch in string:
#         ascii_code = ord(ch)
#         if ascii_code >= 65 and ascii_code <= 90:
#             ascii_code = ascii_code + 32
#             new_char = chr(ascii_code)
#             result += new_char
#         elif ascii_code >= 97 and ascii_code <= 122:
#             ascii_code = ascii_code - 32
#             new_char = chr(ascii_code)
#             result += new_char
#         else:
#             result += ch
#     return result

# a = "ANIruDh$#^*   !@@#@000ADWKAhhdkwa   ___++"
# print(a)
# print(swapcase(a))
        