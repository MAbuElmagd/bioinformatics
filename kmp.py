def lps(p):
    m=len(p)
    l=[0]*m
    i=1
    j=0
    while i<len(p):

       
        if p[i]==p[j]:
           j=j+1
           l[i]=j
           i=i+1
        else :
            if j==0 :
                l[i]=0
                i=i+1
            else :
                j=l[j-1]
    return l
def kmp(lps,p,t):
    i=0
    j=0
    while i<len(t):
        if t[i]==p[j]:
            if j==(len(p)-1):
               print("found in index :")
               print(i-j)
               break
            else:
                j=j+1
                i=i+1
        else :
            if j==0 :
                i=i+1
            else :
                j=lps[j-1]

print("abcaby")
print(lps("abcaby"))
kmp(lps("abcaby"),"abcaby","abxabcabcaby")
