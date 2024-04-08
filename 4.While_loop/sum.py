i=1
total=0
while i<=10:
   total= total+i
   i+=1
print(total )


"""
start
end
Print how many even numbers are there
"""

def countEven(start, end):
    i = start
    count = 0
    sum=0
    while i <= end:
        if i % 2 == 0:
            count = count + 1
      
        i += 1
        sum+=i
    return count

print(countEven(1, 5))
print(f"Number of even numbers = {countEven(1, 5)} {sum}")
