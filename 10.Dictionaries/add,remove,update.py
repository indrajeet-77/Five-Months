marks={ "Sci":88,
       "math":18,
       "hindi":77,
      }

#update/add
print(marks)
marks["math"]=100#update
marks["xyz"]=200#exists nhi krta toh add 

#delete
del marks["Sci"]
print(marks)