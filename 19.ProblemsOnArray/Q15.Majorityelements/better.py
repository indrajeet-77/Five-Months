# Tc=O(2N)==O(N)

# Sc=O(N) 


def majorityelement(arr):
    frquency_map=dict()
    n=len(arr)
    for  i in range(0,n):
        frquency_map[arr[i]]=frquency_map.get(arr[i],0)+1
    # print(frquency_map)
    for k,v in frquency_map.items():
        if v>n//2:
            return k
x=[1,2,2,2,5,6,6,6,6,6,6]
print(majorityelement(x))