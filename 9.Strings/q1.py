a="Hello WOOrLLLDd"

#Via value
count=0
for i in a:
    if i=="o" or i=="O":
        count+=1
print(count)

#Via Index

count=0
for index in (0,len(a)):
    if a[index]=="O" or a[index]=="o":
        count+=1
print(count)