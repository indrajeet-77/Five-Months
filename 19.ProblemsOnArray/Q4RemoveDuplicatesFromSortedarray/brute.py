# tc=O(2N)
# sc=O(N)
def removeduplicates(arr):
    n=len(arr)
    my_dict=dict()
    for i in range(0,n):
        my_dict[arr[i]]=0
    j=0
    for key in my_dict:
        arr[j]=key
        j+=1
    
    # This is optional for loop cause i wanted to put 0's after removing duplicates
    for i in range(len(my_dict),n):
        arr[i]=0
    return arr

x=[1,2,1,2,2,2,3,4,4,5,5,9,10]
print(removeduplicates(x))     