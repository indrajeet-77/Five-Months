# Q1. Given a list of strings, concatenate them into a single string separated
# by spaces. For example, given the input ["Hello", "World", "Python"], the
# output should be "Hello World Python".
# Make a list on your own.
# Don't use the JOIN function.

# list_string=["Hello", "World","python"]
# n=len(list_string)
# result=''
# for i in range(0,n):
#      result+=list_string[i]+" "
# print(result)



# Q2. Write a program to rotate the characters in a string by a given number
# of positions. For example, given the input "abcdef" and rotation of 2, the
# output should be "efabcd".
# Ask string and rotation from the user.    

# def rotate_string(my_string:str,k:int)->str:
#     for _ in range(k):
#         my_string=my_string[-1]+my_string[:-1]
#     return my_string
# x="abcdef"
# k=2
# print(rotate_string(x,k))


# Q3. Write a Python program to convert a given string to all uppercase if it
# contains at least 2 uppercase characters in the first 4 characters.
# Input: pyTHon
# Output: PYTHON
# Input: helLo
# Output: helLo

# def convertToUppercase(my_string:str):
#     uppercount=0
#     result=''
#     n=len(my_string)
#     for ch in range(n):
#         asc=ord(my_string[ch])
#         if asc>=65 and asc<=90:
#             uppercount+=1
#     if uppercount>=2:
#         for ch in range(n):
#             asc1=ord(my_string[ch])
#             if asc1>=97 and asc1<=122:
#                      asc2=asc1-32
#                      newch=chr(asc2)
                  
#             if asc1>=65 and asc1<=90:
#                      asc2=asc1
          
#                      newch=chr(asc2)
#             result+=newch
#     return result
# x=input("Enter: ")
# print(convertToUppercase(x))


# Q4. Create a dictionary that counts the frequency of words in a given
# string. Ask string from user.
# Example 1
# Input String: "The sun is shining and the weather is nice"
# Output:
# {
# 'The': 1,
# 'sun': 1,
# 'is': 2,
# 'shining': 1,
# 'and': 1,
# 'the': 1,
# 'weather': 1,
# 'nice': 1
# }

            
# def countFrequency(my_string:str):
#     my_dict=dict()
#     words=my_string.split()
#     for word  in words:
#         my_dict[word]=my_dict.get(word,0)+1
#     return my_dict
# x=input('Enter string: ')
# print(countFrequency(x))
        
        
# Q5. Write a Python program to map two lists into a dictionary. Everything
# in both lists should be unique.
# Example 1
# list1 = ['red', 'green', 'blue']
# list2 = ['#FF0000','#008000', '#0000FF']
# Output: {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}

# list1 = ['red', 'green', 'blue']
# list2 = ['#FF0000','#008000', '#0000FF']
# my_dict=dict()
# for i in range(len(list1)):
#     my_dict[list1[i]]=list2[i]
# print(my_dict)



# Q6. Write a Python program to convert string values of a given dictionary
# into integer/float data types.
# Example 1:
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# Output:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# def convo(data:list[dict]):
    
#  for d in data:
#     for key, value in d.items():
#          if "." in value:
#                 d[key] = float(value)
#          else:
#                 d[key] = int(value)
     
#     return data


# list2 = [
#     {"x": "10.12", "y": "20.23", "z": "30"},
#     {"p": "40.00", "q": "50.19", "r": "60.99"},
# ]

# output2 = convo(list2)
# print(output2)
    


