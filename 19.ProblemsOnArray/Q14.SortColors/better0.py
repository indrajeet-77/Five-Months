# using dict
# Tc=O(2N)
# SC=O(N)
def sortcolors(arr:list):
    
    n=len(arr)
    freq_map=dict()
    for i in range(n):
        freq_map[arr[i]]=freq_map.get(arr[i],0)+1
    print(freq_map)
    for i in range(0,freq_map[0]):
        arr[i]=0
    for i in range(freq_map[0],freq_map[0]+freq_map[1]):
        arr[i]=1
    for i in range(freq_map[0]+freq_map[1],n):
        arr[i]=2
        
    
x=[2,0,2,1,1,0]
sortcolors(x)
print(x)


        




