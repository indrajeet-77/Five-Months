# WEEK 4 - ASSIGNMENT 6
# SPLITING AND JOINING

# Q1. Ask a string from user. If the length of string is odd, then change all the
# capital letters to small and vice versa, but if the length of string is even,
# reverse the string. Do this using a function and return the output.


# def eveoddrev(string:str):
#    res=str()
#    n=len(string)
#    if n%2!=0:
#      for i in range(0,n):
#          if "a">= string[i] <="z":
#           new_ord=ord(string[i]) -32
#           res=res+chr(new_ord)  
#          elif "A">= string[i]<="Z":
#           new_ord=ord(string[i])+32
#           res=res+chr(new_ord)
#    else:
#       res=string[::-1] 
#    return res
# x=input("Enter string: ")
# print(eveoddrev(x))   

def eveoddrev(string: str):
    res = str()
    n = len(string)
    if n % 2 != 0:
        for i in range(0, n):
            if ord('a') <= ord(string[i]) <= ord('z'):
                new_ord = ord(string[i]) - 32
                res += chr(new_ord)
            elif ord('A') <= ord(string[i]) <= ord('Z'):
                new_ord = ord(string[i]) + 32
                res += chr(new_ord)
    else:
        res = string[::-1]
    return res

x = input("Enter string: ")
print(eveoddrev(x))







# Q2. Write a function which accepts a String as a parameter and return the
# list of words

# def listofwords(string):
#         lw=string.split(" ")
#         return lw
# x=input("Enter: ")
# print(listofwords(x))



# Q3. Write a function which accepts a String as a parameter and return the
# reversed words as a String.

# def reversedWord(string:str)->str:
#     #split  the string into words
#     words= string.split()
#     #here im spliiting the string on basis of space like this ["python", "is ","good"]
#     # print(words)
    
#     #now i have to reverse the ORDER OF WORDS
#     reversed_word=words[::-1]
#     # print(reversed_word)
#     #it has been reversed by words 
#     #now i have to join the spliited string on the basis of space 
#     reversed_string=' '.join(reversed_word)
#     #here string has been joind 
#     return reversed_string

# x=input("Enter string: ")
# print(reversedWord(x))


# Q4. Ask 5 integers from user. Then ask a single character from user. Print
# those integers separated by that character entered by user.

#ask to sir






# Q 5.Write a function which accepts a String as a parameter and return each
# word being in reverse.
# def reverseWords(my_string:str):
#     #lets split the string on basis of space
#     words=my_string.split()
#     # print(words)
#     #here i have splitted the given string 
#     #so i need to reverse each word of string first
#     reversed_words=[]
#     for word in words:
#         reversed_word=word[::-1]#here each word gets reversed i.e. : python = nohtyp and so on
#         reversed_words.append(reversed_word)
#         #now i  have to join words on basis of space
#     reversed_string = " ".join(reversed_words)
#     return reversed_string
# x=input("Enter the string: ")
# print(reverseWords(x))






# Q 5.Write a function which accepts a String as a parameter and return each
# word being in reverse.

# def reversedWords(string:str):
#  words=string.split()
#  reversed_words=[]
#  for word in words:
#     reversed_word= word[::-1]
#     reversedWords.append(reversed_word)
#  reversed_string= " ".join(reversed_words)
#  return reversed_string

# x=input("Enter string: ")
# print(reversedWords(x))


































