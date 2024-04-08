def add(a,b):#parameter are defined
    
    return a+b
print(add(int(input("ENter value:")),int(input("ENter value:"))))#arguments are sent to functions


# Parameters and Arguments

def addition(a:int, b:int):
    total = a + b
    print(total)

addition(10, 20)
addition("Anirudh", "Khurana")


#sir
# Parameters and Arguments

def addition(a: int, b: int):
    a = 100
    b = 100
    total = a + b
    print(total)

x = 10
y = 20
addition(x, y)
print(x)
print(y)