
def countChars(a:str)->dict[str,int]:
 freq_map=dict()
 n=len(a)

#method 1
# for i in range(n):
#     freq_map[a[i]]=freq_map.get(a[i],0)+1
# print(freq_map)


#method 2
 for i in range(n):
    if a[i] in freq_map:
        freq_map[a[i]]+=1
    else:
        freq_map[a[i]]=1
 return freq_map


a='python is a great language'
print(countChars(a))

