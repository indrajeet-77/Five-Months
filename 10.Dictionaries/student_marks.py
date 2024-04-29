details = {
    "anirudh": [45, 44, 33, 12, 5, 6, 45, 6, 2],
    "sanjay": [67, 89, 96],
    "vandana": [76, 43, 53, 21, 22],
    "vivek": [11, 22, 31, 78, 94],
}
"""
anirudh has scored 320 marks
sanjay has scored 210 marks
...
"""

for name,marks in details.items():
    # no logic
    # total=sum(marks)
    # print(f" {name} has scored {total} marks")
    total=0
    for m in marks:
        total+=m
    print(f"{name} has scored {total} marks")



# this is how u can do with get                                   details = {
#     "anirudh": [45, 44, 33, 12, 5, 6, 45, 6, 2],
#     "sanjay": [67, 89, 96],
#     "vandana": [76, 43, 53, 21, 22],
#     "vivek": [11, 22, 31, 78, 94],
# }


# for name in details.keys():
#     total=0
#     for i in details.get(name):
#         total=total+i
#     print(total)