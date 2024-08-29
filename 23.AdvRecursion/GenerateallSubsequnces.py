def generatesubseq(subset, index):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    generatesubseq(subset, index + 1)
    subset.pop()
    generatesubseq(subset, index + 1)


nums = [3, 2, 1]
result = []
generatesubseq([], 0)
print(result)
