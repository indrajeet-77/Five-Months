# Tc=
# sc=

def stock(arr):
    n=len(arr)
    max_profit=0
    minimum_price=float('inf')
    for i in range(n):
        minimum_price=min(minimum_price,arr[i])
        max_profit=max(max_profit,arr[i]-minimum_price)
    return max_profit
