# marks={ "Sci":88,
#        "math":18,
#        "hindi":77,
#        "english":30,
#        "married":None
       
#       }

#dict is iterable

#traversing keys
# print(marks.keys())
#traversing values
# print(marks.values())

#keys chaiye toh ye
# all_keys=marks.keys()
# print(all_keys)

# for k  in all_keys:
#     print(f"key{k} value={marks[k]}")
    
   #values chaiye toh ye 
# for v in marks.values():
#     print(v)

#dono chaiye toh ye
# for k,v in marks.items():
#     print(f"keys= {k} : values={v}")
    
    
#sir given   
marks = {
    "science": 78,
    "english": 91,
    "maths": 56,
    "hindi": 84,
}
#for keys
# for k in marks.keys():
#     print(f"Key = {k} Value = {marks[k]}")

#for values
# for v in marks.values():
#     print(v)

#for both
# for k, v in marks.items():
#     print(k, v)


#proper way to traverse 
for sub in marks:
    print(sub,marks[sub])