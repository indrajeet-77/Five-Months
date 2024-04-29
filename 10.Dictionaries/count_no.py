#count frequency of elements using dict
# arr=[1,4,5,5,4,6,3,1,1,2,5,2,1,6,3,9]
# n=len(arr)
# Freqency_map=dict()

# for i in range(n):
#     if arr[i] in Freqency_map:
#         Freqency_map[arr[i]]+=1
#     else:
#         Freqency_map[arr[i]]=1
    
# print(Freqency_map)


# OR

# arr = [1, 4, 5, 5, 4, 6, 3, 1, 1, 1, 2, 9]
# n = len(arr)
# freq_map = dict()  # { }
# for i in range(n):
#     freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
#     #freq_map may ka arr[o] =freq_map.get(arr[o],0)+1
# print(freq_map)






#count no of occurances

arr=[1,2,1,2,3,2,4,2,3,4,5,5,6,2,1,6,7,1]
freq_map=dict()
n=len(arr)
for i in range(n):
    if arr[i] in freq_map:
        freq_map[arr[i]]+=1
    else:
        freq_map[arr[i]]=1
print(freq_map)