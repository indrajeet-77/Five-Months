# Tc=
# sc=


def canmake(bloomday,day,k,m):
    count=0
    totalNumberOfBoquet=0
    for i in range(len(bloomday)):
        if bloomday[i]<=day:
            count+=1
            if count==k:
                totalNumberOfBoquet+=1
                count=0
            else:
                count=0
        return totalNumberOfBoquet>=m
def minimumdaystobloom(bloomday,m,k):
    for i in range(1,max(bloomDay)):
        possible=canmake(bloomday,i,m,k)
        if possible:
            return i
bloomDay = [7,7,7,7,13,11,12,7]
m = 2
k = 3
print(minimumdaystobloom(bloomDay,m,k)) 