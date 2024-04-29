details = {
    "science": 78,#("science",78) <----x | x[1]
    "english": 91,
    "maths": 56,
    "chem":99
    
}
new_details=sorted(details.items(),key=lambda x:x[1])
print(details)
print(dict(new_details))




#Sir Given

# dict_items([('physics', 56), ('chemistry', 19),
# ('maths', 91), ('algebra', 74), ('history', 74)])
details = {
    "physics": 56,  # ('physics', 56) <---x | x[1]
    "chemistry": 19,
    "maths": 91,
    "algebra": 74,
    "history": 74,
}
new_details = dict(sorted(details.items(), key=lambda x: x[1]))
print(details)
print(new_details)

#Special case  where we can type covo the list of tuples into dict
x = [("physics", 55), ("chemistry", 11), ("history", 99)]
print(dict(x))