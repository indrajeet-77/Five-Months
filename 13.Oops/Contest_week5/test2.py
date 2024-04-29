# Q1. Create a function named oddCharacters which takes a string as a
# parameter. Now return a list of characters which appears odd times in that
# string.
# def oddchars(my_string:str):
#  l=[]
#  for ch in my_string:
#     if my_string.count(ch)%2!=0:
#         # result+=ch
#         l.append(ch)      
#  return l 
# x="hello"
# print(oddchars(x))





# Q2. Create a function named arrangeChars which takes a string as a
# parameter. Now return a string with max frequency chars at start.

#Frequency mapping
# def arrangechars(string:str):
#     n=len(string)
#     result=str()
#     freq_map=dict()
#     for i in range(n):
#         freq_map[string[i]]=freq_map.get(string[i],0)+1
#     sorted_freq_map=dict(sorted(freq_map.items(),key=lambda x:x[1],reverse=True))
#     for key , value in sorted_freq_map.items():
#         result+=key*value
#     return result

# x="heellllloooo"
# print(arrangechars(x))



# Q3. Given a string S, containing numeric words, the task is to convert the
# given string to the actual number.
# Input: S = “zero four zero one”
# Output: 0401
# Input: S = “four zero one four”
# Output: 4014


          
# s="One two three four"
# s=s.lower()
# help_dict={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
# res= "".join(help_dict[ele] for ele in s.split())
# print(res)


# Q4. Convert Snake case to Pascal case.
# Input: python_is_great
# Output: PythonIsGreat
# Input: we_are_learning_python_programming
# Output: WeAreLearningPythonProgramming


        
# string="python_is_great"
# #here i capitalized first letter of each word using  .title()
# s=string.title()
# #here i splitted on basis of underscore
# s=s.split("_")
# #so after splitting it returns a list ,but i need a string which is joined so i used "".join
# s= "".join(s)

# #i used here starts with function and .upper() function to let the string starts with upper letter/ i guess without it will also work
# # # s.startswith(s.upper()) 
# print(s)



    
# Q5. Write a Python program to capitalize the first and last letters of each
# word in a given string.
# Input: delhi is best city with 0 AQI
# Output: DelhI IS BesT CitY WitH 0 AqI


# s = "python is great language"
# s3 = s.split(" ")

# final_output = ""

# for word in s3:
#     # Capitalize the first and last letter of the word
#     capitalized_word = word[0].upper() + word[1:-1] + word[-1].upper()
#     # Append the capitalized word to the final output
#     final_output += capitalized_word + " "

# # Output the final result
# print(final_output.strip())










        

