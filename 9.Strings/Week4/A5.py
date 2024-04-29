#         num is from 48 to 57
#         # 65-90 for capital alpha
#         # 97 -122 for small alpha
#         # 32 for space



# Q1. Write a function in Python that counts the number of digits in a given
# string using ASCII codes

# def count_dig(string):
#     count=0
#     for ch in string:
#         ascii_1=ord(ch)
#         if ascii_1>=48 and ascii_1<=57:
#             count+=1
#     return count
# x= input("ENter a string: ")
# print(count_dig(x))



# Q2. Develop a Python script that counts how many letters are in a string by
# checking ASCII values.

# def countLetters(string):
#     count=0
#     for ch in string:
#         asc=ord(ch)
#         if asc >=65  and asc <=90 :
#             count+=1
        
#         if asc >=97 and asc <=122:
#                 count+=1
#     return count
# x=input("ENter a string: ")
# print(countLetters(x))
        





# Q3. Implement a function in Python to check if a string is alphanumeric by
# examining the ASCII values of its characters.
# Input: "Var123"
# Output: True
#alphanumeric = alphabets+numbers
# def isalphanumeric(string:str)->bool:
#     flag=False
#     for ch in string:
#         asc=ord(ch)
#         if (asc>=65 and asc<=90 )or (asc>=97 and asc <=122) or (asc>=48 and asc<=57):
#             flag=True
#         else:
#             return flag
#     return flag
# x=input("enter a string: ")
# print(isalphanumeric(x))





# Q4. Write a Python function that toggles the case of each letter in a string
# (converts uppercase to lowercase and vice versa) using ASCII values.
# Input: "Python3.8"
# Output: "pYTHON3.8"

# def togglecase(string):
#     result=str()
#     for ch in string:
#         asc=ord(ch)
#         if asc >=65 and asc<=90:
#             asc+=32
#             newch=chr(asc)
#             result+=newch
#         elif asc >=97 and asc<=122:
#             asc-=32
#             newch=chr(asc)
#             result+=newch
#         else:
#             result+=ch
#     return result
# x=input("Enter string: ")
# print(togglecase(x))


# Q5. Write a Python script that replaces each non-alphabetic character in a
# string with a space, using ASCII to determine character types.
# Input: "Hello, World!"
# Output: "Hello World "

# def replaceWithSpace(string:str):
#     result=""
#     for ch in string:
#         asc=ord(ch)
#         if(asc>=65 and asc<=90) or (asc>=97 and asc<=122):
#             result+=ch
#         else:
#             result+=" "
#     return result

# x= input("enter string: ")
# print(replaceWithSpace(x))

#sir
# def rem_s(string):
#     res=" "
#     for ch in string:
#         asc=ord(ch)
#         if (asc>=65 and asc <=90) or (asc>=97 and asc<=122):
#             res+=ch
#         else:
#             res+=" "
#     return res
# print(rem_s("hdeh!,jhds"))





# Q6. Write a Python program that computes the sum of the ASCII values of
# all characters in a string.

# def sumOfAscii(string):
#     sum=0
#     for ch in string:
#         asc=ord(ch)
#         sum+=asc
#     return sum
# x=input("Enter a string : ")
# print("Sum of asci of all char in string =",sumOfAscii(x))




# Q7. Implement a Python function that checks if a string contains any
# special characters (non-alphanumeric) by using ASCII codes.
# Input: "password123!"
# Output: True


# def specialChar(string: str)->bool:
#     for ch in string:
#         asc=ord(ch)
#         if (asc>=32 and asc <=47) or (asc>=58 and asc<=64) or (asc>=91 and asc<=96) or (asc>=123 and asc <=126):
#             return True
#     return False

# x=input('enter string: ')
# print(specialChar(x))




# Q8. Write a function in Python that removes all numeric characters from a
# string by checking their ASCII codes.
# Input: "Abc123"
# Output: "Abc"



# def removeNumericChars(string:str):
#     res=''
#     for ch in string:
#         asc=ord(ch)
#         # print(asc)
#         if (asc>=65 and asc<=90 ) or (asc>=97 and asc<=122):
#             newch=chr(asc)
#             res+=newch
#     return res

# x=input("Enter string: ")
# print(removeNumericChars(x))
    
        

 
# .9 Develop a Python program that finds the character with the maximum
# ASCII value in a given string.
# Input: "hello"
# Output: 'o' (highest ASCII character in the string)


# def maxCharAsci(string:str):
#     store=0
#     nwch=str()
#     for ch in string:
#         asc=ord(ch)
#         if(asc>=65 and asc<=90) or (asc>=97 and asc<=122):
#             if asc>store:
#                 store=asc
#                 nwch=chr(store)
#     return nwch
# x= input("enter string: ")
# print(maxCharAsci(x))
            