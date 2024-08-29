def maxPointsCanObtainFromCards(cards,k):
    n=len(cards)
    left_sum=0
    right_sum=0
    result=0
    for i in range(k):
        left_sum+=cards[i]
    result=left_sum
    right_index=n-1
    for i in range(n-1,-1,-1):
        right_index+=cards[right_index]
        max