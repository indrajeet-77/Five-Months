# Q1. Here’s a students data and their marks.
# student_data = {
# "Alice": [85, 90, 88, 92, 89],
# "Bob": [78, 82, 79, 81, 80],
# "Charlie": [92, 95, 88, 85, 91],
# "Diana": [76, 80, 79, 82, 85],
# "Eva": [88, 92, 85, 90, 87],
# "Frank": [83, 85, 80, 86, 88],
# "Gina": [90, 87, 92, 88, 86],
# }
# Display the name of student and total marks in ascending order.
# OUTPUT:
# Bob has scored 400
# Diana has scored 402
# Frank has scored 422
# Eva has scored 442
# Gina has scored 443
# Alice has scored 444
# Charlie has scored 451

# student_data = {
# "Alice": [85, 90, 88, 92, 89],
# "Bob": [78, 82, 79, 81, 80],
# "Charlie": [92, 95, 88, 85, 91],
# "Diana": [76, 80, 79, 82, 85],
# "Eva": [88, 92, 85, 90, 87],
# "Frank": [83, 85, 80, 86, 88],
# "Gina": [90, 87, 92, 88, 86],
# }
# new=dict()
# for keys,values in student_data.items():
#     totalscore=sum(values)
#     new[keys]=totalscore
# new1=sorted(new.items(),key=lambda x:x[1])
# for item in new1:
#      name,score=item
#      print(f"{name} has scored {score}")





# Q2. Here’s student data.

# student_data = {
# "Ella": {"age": 20, "marks": [85, 78, 92, 89, 91]},
# "Max": {"age": 22, "marks": [79, 85, 88, 90, 87]},
# "Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]},
# "Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]},
# "Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]},
# "Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]},
# "Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]},
# }
# Generate the outcome like this.

# Liam has scored 402
# Noah has scored 422
# Max has scored 429
# Ella has scored 435
# Ava has scored 442
# Emma has scored 443
# Sophia has scored 451


# student_data = {
# "Ella": {"age": 20, "marks": [85, 78, 92, 89, 91]},
# "Max": {"age": 22, "marks": [79, 85, 88, 90, 87]},
# "Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]},
# "Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]},
# "Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]},
# "Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]},
# "Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]},
# }


# new_details=dict()
# total_marks = {}
# for name, data in student_data.items():
#     total_marks[name] = sum(data["marks"])
# new_details=sorted(total_marks.items(),key=lambda x: x[1])
# for name,marks in new_details:
#     print(f"{name} has scored {marks}")




# Q3
student_data = [
["Samantha", 18, "New York", 420],
["David", 25, "Los Angeles", 380],
["Sophie", 22, "Chicago", 390],
["Michael", 20, "Houston", 410],
["Liam", 19, "Phoenix", 430],
["Olivia", 21, "Philadelphia", 400],
["Daniel", 23, "San Antonio", 375],
]
sorted_data=sorted(student_data,key=lambda x: x[-1])
print(sorted_data)
    