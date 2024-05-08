# 1. Print 1 to N without Loop

def fun(i,n):
    if i>n:
        return
    print(i)
    fun(i+1,n)
    
fun(1,10)

#print i to 1 uisng (i+1)

        