"""
function which takes one int arg
return str <odd,evem
"""

def eve_odd(num:int)->str:
    if num%2==0:
        return "even"
    #in here the second return will run if only the if stament didnt works 
    return "odd"
print(eve_odd(99))