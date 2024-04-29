a="golu"
a+='hehe'
print(a)#is is immutable but it will run cause we are reassigning values so id change hogi

# result=''
result=str()
while True : #for infi running
    xyz=input("Enter a char : ")
    if xyz=="q" or xyz=="Q":
    # if xyz in ["q", "Q"]:
        break
    result+=xyz
print(result)
    