#    012345678
# s="abcdzabcd"
# op=5
def maxlensub(s: str) -> int:
    n = len(s)
    l = 0
    r = 0
    hash_map = dict()
    maxlen = 0
    while r < n:
        # we will check window is valid or not
        if s[r] in hash_map:
            # if s[r] exists we will calculate the position of l
            l = max(hash_map[s[r]] + 1, l)
        # Adding s[r] and r th index to dict
        hash_map[s[r]] = r
        # calculating the maxlen (not using count)
        maxlen = max(maxlen, r - l + 1)
        r += 1
    return maxlen


x = "bbbbb"
print(maxlensub(x))
