# tc=O(N*2)
# sc=O(1)
# sliding window  problem
def sumSubarrayMins(fruits):
    n = len(fruits)
    maxlen = 0
    for i in range(0, n):
        myset = set()
        for j in range(i, n):
            myset.add(fruits[j])
            if len(myset) > 2:
                break
            maxlen = max(maxlen, j - i + 1)
    return maxlen


f = [1, 1, 2, 3, 3, 1]
print(sumSubarrayMins(f))
