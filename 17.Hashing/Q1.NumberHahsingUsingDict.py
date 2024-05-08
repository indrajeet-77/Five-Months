
x=[5,2,1,4,5,5,5,1,3,5,3]
hash_dict={}
for num in x:
    hash_dict[num]=hash_dict.get(num,0)+1
print(hash_dict)
number=int(input("Enter a num to count: "))
print(hash_dict.get(number,0))
