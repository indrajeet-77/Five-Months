# tc=O(N**2)/ O(N*(N+1)/2)
# sc=O(1)/O(3)
def NumberOFSubstringContainingAllChars(s: str) -> int:
    count = 0
    n = len(s)
    for i in range(0, n):
        myset = set()
        for j in range(i, n):
            myset.add(s[j])
            if len(myset) == 3:
                count += 1
    return count


x = "bbacba"
print(NumberOFSubstringContainingAllChars(x))
