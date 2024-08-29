# Find length of longest substring with no repitation
# s="abcdzabcd"
# maxlen=5
# TC=Sum of n natural nums= O(N*(N+1)/2)==O(N**2)
# SC=O(N)


def maxlenofsubstring(s: str) -> int:
    maxlen = 0
    n = len(s)
    for i in range(0, n):
        isSeen = set()
        for j in range(i, n):
            if s[j] in isSeen:
                break
            isSeen.add(s[i])
            maxlen = max(maxlen, j - i + 1)
    return maxlen


s = "abcdzabcd"
print(maxlenofsubstring(s))
