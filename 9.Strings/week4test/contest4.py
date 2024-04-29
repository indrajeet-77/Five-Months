# Q1. Create a python function named isPalindrome which accepts a string
# as a parameter and return True if its a palindrome. Palindrome are words
# which is same when read from start and same when read from the end

# def isPalindrome(string:str):
#     flag=False
#     n= len(string)
#     for ch in range(0,n):
#         asc=ord(string[ch])
#         for lsch in range(n-1,ch+1,-1):
#             asc_1=ord(string[lsch])
#             if asc==asc_1:
#                 flag=True
#         return flag
#     return flag
# x=input("Enter string: ")
# print(isPalindrome(x))



# Q2. Keep asking characters from user until he presses q on the keyboard.
# Change all the capital letters to small, and all the small letters to capital.

#Ask to sir

# def changeCaseOnPressingQ(string:list)->str:
#     string1="".join(string)
#     result=str()
#     n=len(string1)
#     for ch in range(0,n):
#         asc=ord(string1[ch])
#         if asc>=65 and asc<=90:
#             new_asc=asc+32
#             new_word=chr(new_asc)
#             result=result+new_word
#         elif asc>=97 and asc<=122:
#             new_asc=asc-32
#             new_word=chr(new_asc)
#             result=result+new_word 
#         else:
#             result+=str(ch)
#     return result
    
# input_chars=[] 
# while True:
#     char = input("Enter a char: ")
#     input_chars.append(char)
#     if char == 'q' or char=="Q":
#         input_chars.pop()  # Remove 'q'
#         print(changeCaseOnPressingQ(input_chars))
#         break





# Q3. Python Program to remove all duplicates from a given string.

# def removeduplicates(string:str):
#     result=str()
#     n=len(string)
#     for ch in range(0,n):
#         if string[ch] not in result:
#             result+=string[ch]
#     return result
# x=input("Enter string: ")
# print(removeduplicates(x))



# Q4.Ask a sentence from user. Then ask a integer k from user. Print all the
# words which are greater or equal to k.



# def k_long_sentence(sentence:str,k:int)->str:
#     splitted_sen=sentence.split()
#     # print(splitted_sen)
#     for ch in splitted_sen:
#         if len(ch)>=k:
#             print(ch,end=" ")

# sentence=input("Enter sentence: ")
# k=int(input("Enter K: "))
# k_long_sentence(sentence,k)




# Q6. Make a password strength function. It will accept a string from user.
# Return True if it is a strong password.
# Strong password has these characteristics.
# Minimum 8 character
# Minimum 1 uppercase alphabet
# Minimum 1 lowercase alphabet
# Contains at least 1 special symbol (any symbol)
# Minimum 1 digit

def passwordStrength(my_string:str)->bool:
   has_uppercase=False
   has_lowercase=False
   has_dig=False
   has_special=False
   
   for ch in my_string:
       if ch.isupper():
           has_uppercase=True
       elif ch.islower():
           has_lowercase=True
       elif ch.isdigit():
           has_dig=True
       elif not ch.isalnum():
           has_special=True
   if(
        len(my_string)>=8
        and has_uppercase
        and has_lowercase
        and has_dig
        and has_special
    ):
       return True
   else:
       return False
   
password=input("enter pass: ")
print(passwordStrength(password))

           
           
        
        