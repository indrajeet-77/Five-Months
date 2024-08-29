# TC=O(N)
# SC=O(1)/O(3)


def NumberOFSubstringContainingAllChars(s: str) -> int:
    n = len(s)
    count = 0
    i = 0
    chars = {"a": -1, "b": -1, "c": -1}
    while i < n:
        chars[s[i]] = i
        if chars["a"] != -1 and chars["b"] != -1 and chars["c"] != -1:
            count += min(chars.values()) + 1

        i += 1
    return count
x='bbacba'
print(NumberOFSubstringContainingAllChars(x))