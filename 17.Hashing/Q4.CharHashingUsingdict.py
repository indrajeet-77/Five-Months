string='aerrropllane'
dict_map={}
for ch in string:
    dict_map[ch]=dict_map.get(ch,0)+1
print(dict_map)
char=input("Enter a char to count: ")
print(dict_map.get(char,0))