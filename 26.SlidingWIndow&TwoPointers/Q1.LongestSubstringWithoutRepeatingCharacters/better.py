# Tc=O(N)
# Sc=o(N)
# me
def maxlensubstring(s: str) -> int:
    n = len(s)
    l = 0
    r = 0
    s1 = s[r]
    maxlen = 1
    while r < n:
        if s[r] not in s1:
            s1 += s[r]
            maxlen = max(maxlen, r - l + 1)
        if s[r] in s1:
            l = max(r, l)
        r += 1
    return maxlen


s = "abcdzabcd"
print(maxlensubstring(s))
