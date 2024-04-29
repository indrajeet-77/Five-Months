# Q1. Write a function that takes a dictionary and a key, and returns True if
# the key is found in the dictionary, otherwise False

# def isIndict(my_dict:dict,k:str)->bool:
#      if k in my_dict.keys():
#          return True
#      return False
# print(isIndict({'ONE':1,'TWO':2},"THREE"))




# Q2. Given two dictionaries, write a function to merge them into a new
# dictionary. If there is any overlap of keys, the value from the second
# dictionary should overwrite the one from the first dictionary.
# Dictionary 1:
# {'apple': 3, 'banana': 5, 'cherry': 7}
# Dictionary 2:
# {'banana': 8, 'orange': 10, 'apple': 9}
# Expected Output:
# {'apple': 9, 'banana': 8, 'cherry': 7, 'orange': 10


# def mergeTwo(my_dict1,my_dict2)->dict:
#     merged=my_dict1.copy()
#     for k, v in my_dict2.items():
#         merged[k]=(v)
#     return merged
    
#     # #SIR
#     # merged = my_dict1.copy()  # Start with a copy of the first dictionary
#     # for key, value in my_dict2.items():
#     #     merged[key] = ( value  )# Set the value from the second dictionary, overwriting if key exists)
#     # return merged
# x= {'apple': 3, 'banana': 5, 'cherry': 7}
# y={'banana': 8, 'orange': 10, 'apple': 9}
# print(mergeTwo(x,y))
    



# Q3. Write a function that updates the values of a dictionary by multiplying
# them by a given factor only if the value is an integer

# def updict(fac:int):
#     my_dict={"a":4,"b":7.8,"c":True,"d":7}
#     for v in my_dict:
#         if type( my_dict[v])==int:
#             my_dict[v]=my_dict[v]*2
#     return my_dict

# fac=int(input("enter : "))
# print(updict(fac))



# Q4. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are squares of the keys.
# def create_sq():
#     sq_dict=dict( )
#     for i in range(1,16):
#         sq_dict[i]=i**2
#     return sq_dict
# print(create_sq())





# Q5. Given a dictionary, write a function that returns a new dictionary
# containing only the keys that have values of type str.


# def string_dict(my_dict:dict):

#  str_mydict=dict()

#  for values in my_dict:
#     if type(my_dict[values])==str:
#         str_mydict[values]=my_dict[values]
#  return str_mydict

# my_dict={"Name":"Indrajeet", "Age":22,"Gender":"Male", "Phone":7620711052}
# print(string_dict(my_dict))





# Q7. Write a Python function that takes a dictionary as input where the
# values are lists of integers. The function should return a new dictionary
# where the values are lists containing only the even integers from the
# original lists

# def even_dict(my_dict:dict):



#  eve_dict=dict()
#  for keys in my_dict:
#     eve_dict[keys]=[num for num in my_dict[keys] if num%2==0]
#  return eve_dict


# input_dict={"a":[1,2,3,4,5],"b":[6,7,8,9,10]}
# print(even_dict(input_dict))




# Q8. Write a Python program to combine two dictionary by adding values
# for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}
    
# def addtwodictbycommanval(d1:dict,d2:dict):
#     d3=dict()
#     for key in d1 | d2:
#         d3[key]=d1.get(key,0)+d2.get(key,0)
#     return d3

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(addtwodictbycommanval(d1,d2))

# Q9. Write a Python program to create a dictionary of keys x, y, and z where
# each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# Output
# 15
# 25
# 35

# my_dict={
# "x":list(i for i in range(11,20)),
# "y":list(i for i in range(21,30)),
# "z":list(i for i in range(31,40))
# }
# for k in my_dict:
#     fifth=my_dict[k][4]
#     print(fifth)







# Q10. Store name as a Key, and 5 marks in a List as a value in dictionary.
# Store details of at least 5 students. Print the total marks with percentage
# of each and every student.



# details={
#     "Anirudh":[98,97,96,92,80],
#     "Abhishek":[80,76,82,90,56],
#     "Rohan":[78,98,67,66,77],
#     "Rahul":[77,88,99,66,55],
#     "Rehan":[99,91,87,34,56]
#          }
# for name, marks in details.items():
#     total=sum(marks)
#     percentage=(total/5)
#     print(f"Name={name}, total={total}, percentage={percentage:.2f}")
    
    

# Q11. Given a dictionary with key-value pairs, remove all the keys with
# values greater than K, including mixed values.
# Input : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘xyzx’ : ‘CS’}, K = 7
# Output : {‘Gfg’ : 3, ‘for’ : 6, ‘xyzx’ : ‘CS’}
# Explanation : All values greater than K are removed. Mixed value is
# retained.
# Input : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘qqqq’ : ‘CS’}, K = 1
# Output : {‘qqqq’ : ‘CS’}
# Explanation : Only Mixed value is retained
   
# k=int(input("Enter k: "))
# new=dict()
# test_dict = {"Gfg" : 3, "is":7, "best" : 10, "hehe" : 6, "xyzx" : "CS" }
# for key in test_dict.keys():
#     if type(test_dict[key])==int:
#      if test_dict[key] <k :
#         new[key]=test_dict[key]
#     else:
#         new[key]=test_dict[key]
# print(new)
        



# Q12. A Python dictionary contains List as a value. Write a Python program
# to clear the list values in the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}


# orignal_dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for key in orignal_dict.values():
#     key=key.clear()
# print(orignal_dict)