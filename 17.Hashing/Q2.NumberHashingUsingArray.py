# lst=[5,3,5,3,4,5,3,5,1,3,5,3,5]
# n=len(lst)
# hash_map=[0]*n
# for num in lst:
#     hash_map[num]+=1
#     #here im using 5 ,3,4 etc which are elements of list ,so im using it as indexes of hash map and hash map with those respective
#     # indexes are by defset as 0 and im ind=crementing it by 1 as it counts 
# number=int(input("Enter  number to count: "))
# print(hash_map[number])

# Prestoring TC= O(N)
# fetching TC= O(M)
#total TC= O(M+N)


def numberHashing(arr:list,num:int)->int:
    n=len(arr)
    hashmap=[0]*n
    #pre storing
    for number in arr:
        hashmap[number]+=1
    return hashmap[number]
array=[int(i) for i in input("Enter elemets of array: ").split(",")]
num=int(input("Enter a number to count ,which exits in array : "))
#fetching
print(numberHashing(array,num))