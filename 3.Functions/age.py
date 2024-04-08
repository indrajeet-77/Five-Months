# def vote(age:int)->str:
#     if age<18:#write the negative condition first
#         return "You can not vote"
#     return "You can vote"
# print(vote(18))

def vote(age:int)->None:
    if age<18:
     print("You can not vote")
     return#bhr chale jao function k
    print("You can vote")
vote(15)