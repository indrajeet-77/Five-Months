def findKRotation(arr, n):
    Rotationcount = 0
    prev = 0
    nex = 1
    for i in range(0, n - 1):
        if arr[prev] >= arr[nex]:
            Rotationcount += 1
        prev += 1
        nex += 1
    return Rotationcount


x = [5, 4, 3, 1, 2]
print(findKRotation(x, 5))
