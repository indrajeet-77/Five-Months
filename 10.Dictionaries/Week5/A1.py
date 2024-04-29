# Q1. Make a dictionary with keys as subject name (physics, chemistry, etc.)
# and values as their marks. Print the highest marks scored.

# my_dict = {'Phy': 90, 'chem': 72, 'maths':99}

# for marks in my_dict:
#     high_marks=0
#     if my_dict[marks]> high_marks:
#         high_marks=my_dict[marks]
   
# print(f"highest marks scored={high_marks}")
 
 
# Q2. Make a dictionary with keys as subject name (physics, chemistry, etc.)
# and values as their marks. Print the name of the subject with highest marks
# scored   

# my_dict={"phy":99,"chem":80,"maths":97}
# max=0
# for sub,marks in my_dict.items():
#     if marks>max:
#         max=marks
#         print(f"{sub}")


# Q3. Make a dictionary with keys as subject name (physics, chemistry, etc.)
# and values as their marks. Print the name of the subject which has marks
# more than passing marks (above 33).

# my_dict={"phy":40,"chem":27,"maths":12}
# max=33
# for sub,marks in my_dict.items():
#     if marks>max:
#         max=marks
# print(f"{sub} and {max}")



# Q5. Write a Python program to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x)

# my_dict=dict()
# n=int(input("Enter the value of n"))
# for i in range(1,n+1):
#     my_dict[i]=i**2
# print(my_dict)



# Q6. Write a Python program to check if a dictionary is empty or not.
# def isemptydict(my_dict:dict):

#  for e in my_dict.items():
#     if len(my_dict.keys())==0:
#       return True
#     return False
 
# #  (best way)
#  if not my_dict:
#      return True
#  return False

# print(isemptydict({}))





# Q7. Python program to find the size of a Dictionary. Basically print how
# many total key-value pair are there.

# def sizeOfDict(my_dict:dict):
#     n=len(my_dict.items())
#     return n

# print("Size of dictionary is: ",sizeOfDict({"one":1,"two":2}))