a=(54,11,33,45,66)
print(f" id of a ={id(a)}")
b=list(a)

b.append(100)

print(b)

a=tuple(b)
print(f" id of a ={id(a)}")
print(a)