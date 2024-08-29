# m=number of boquets
# k=number of adj flowers
# day=mid
# bloomday=array of
def canmakeornot(bloomday, day, m, k):
    totalboquet = 0
    count = 0
    flag = False
    for i in range(len(bloomday)):
        if bloomday[i] <= day:
            count += 1
            if count == k:
                totalboquet += 1
                count = 0
        else:
            count = 0
        if totalboquet >= m:
            flag = True

    return flag


# def minimaxi(bloomday):
#     mini=bloomDay[0]
#     maxi=bloomDay[0]
#     for i in range(0,len(bloomday)):
#         if bloomday[i]>maxi:
#             maxi=bloomDay[i]
#         if bloomday[i]<mini:
#             mini=bloomday[i]
#     return


def minbloomday(bloomday, m, brutk):
    low = min(bloomday)
    high = max(bloomday)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        ps = canmakeornot(bloomday, mid, m, k)
        if ps:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans


bloomDay = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3
print(minbloomday(bloomDay, m, k))
