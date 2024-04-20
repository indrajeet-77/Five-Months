#mutable objects pass  by ref se hote h pass
from typing import List
def change(l1:List):
    l1[0]=100
    print(id(l1))
xyz=[34,33,44,555,554]
change(xyz)
print(xyz)
print(id(xyz))

# ismay adress pass hota hai 