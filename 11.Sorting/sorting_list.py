
my_list = [
    ["indrajeet",22],
    ["Akul", 99],  # <---- x   |  x[1]
    ["Karan", 54],
    ["Prateek", 21],
    ["Anirudh", 45],
    
]
def myfunction(x):
    return x[1]
new_list = sorted(my_list, key=lambda x: x[1], reverse=True)#reverse by default false rehta hai so if we set it true then wo decending order may krega sort
new_list=sorted(my_list,key=myfunction)#if we use function we dont need to call the function just pass the reference of function
print(my_list)
print(new_list)