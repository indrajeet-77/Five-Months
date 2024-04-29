#converting list into str
# l=[433,76,"hehe",89]
# print(str(l))
# print(str(l)[0])


# my_list = [334, 54, 56, 54, 432, "Anirudh"]
# # List to String
# print(str(my_list))
# print(str(my_list)[0])
# print(str(my_list)[-1])
my_string = "python432 is a 432good language!"
lst = list(my_string)
# print(lst)
for i in range(0, len(lst)):
    if lst[i] == "o":
        lst[i] = "z"
# print(lst)
print("".join(lst))