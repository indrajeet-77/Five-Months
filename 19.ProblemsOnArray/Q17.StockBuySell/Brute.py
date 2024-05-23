def stockBusysell(arr):
    n=len(arr)
    max_profit=0
    for  i in range(0,n):
        for j in range(i+1,n):
            if arr[j]>arr[i]:
                max_profit=max(arr[j]-arr[i],max_profit)
    return max_profit
x=[7,1,5,3,6,4]
print(stockBusysell(x))