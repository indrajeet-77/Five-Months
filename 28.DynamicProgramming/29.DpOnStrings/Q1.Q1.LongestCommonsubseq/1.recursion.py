def solve(s1,s2,index1,index2):
    if index1<0 or index2<0:
        return 0
    if s1[index1]==s2[index2]:
        return 1 + solve(s1,s2,index1-1,index2-1)
    elif s1[index1]!=s2[index2]:
        return max(solve(s1,s2,index1-1,index2),solve(s1,s2,index1,index2-1))

def longestcommonsubse1uence(string1,string2):
    return solve(string1,string2,len(string1)-1, len(string2)-1)

text1="abcdef"
text2="acxyze"
print(longestcommonsubse1uence(text1,text2))