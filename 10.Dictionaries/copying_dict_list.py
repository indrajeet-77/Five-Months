# my_dict={
#    "science": 78,
#     "english": 91,
#     "maths": 56,
#     "hindi": 84,  
    
# }

# xyz=my_dict
# print(f"xyz= {xyz}")
# print(f"mydict={my_dict}")

# print("-------")

# xyz["hindi"]=100
# print(f"xyz= {xyz}")
# print(f"mydict={my_dict}")


# xyz=my_dict.copy
# print(f"xyz= {xyz}")
# print(f"mydict={my_dict}")

# print("-------")

# xyz["hindi"]=100
# print(f"xyz= {xyz}")
# print(f"mydict={my_dict}")
#basically .copy use krenge toh address(refernce alg hoga) toh kiai may ek ko change kiya toh dusre may nahi hoga













#sir
# my_dictionary = {
#     "science": 78,
#     "english": 91,
#     "maths": 56,
#     "gender":["male,female"]
# }
# xyz = my_dictionary.copy()
# print(id(my_dictionary))
# print(id(xyz))
# print(f"my_dictionary = {my_dictionary}")
# print(f"xyz = {xyz}")
# print("-------")
# xyz["hindi"] = 100
# print(f"my_dictionary = {my_dictionary}")
# print(f"xyz = {xyz}")
# xyz=my_dictionary
# xyz["gender"][0]="gg"
# print(xyz)




import copy
my_dictionary = {
    "science": 78,
    "english": 91,
    "gender": ["Male", "Female"],
}
# xyz = my_dictionary.copy()
# xyz = copy.copy(my_dictionary)  # Shallow Copy
xyz = copy.deepcopy(my_dictionary)  # Deep Copy
print(id(my_dictionary["gender"]))
print(id(xyz["gender"]))

xyz["gender"][0] = "gg"

print(f"my_dictionary = {my_dictionary}")
print(f"xyz = {xyz}")