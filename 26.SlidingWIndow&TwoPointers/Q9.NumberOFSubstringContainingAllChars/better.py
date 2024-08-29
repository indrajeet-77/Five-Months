# Tc=O(N**2)
# SC=O(1)


def NumberOFSubstringContainingAllChars(s: str) -> int:
    count = 0
    n = len(s)
    for i in range(0, n):
        myset = set()
        for j in range(i, n):
            myset.add(s[j])
            if len(myset) == 3:
                count += n - j
                break
    return count


x = "bbacba"
print(NumberOFSubstringContainingAllChars(x))
