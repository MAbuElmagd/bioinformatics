def hash(sub,k):
    h=0
    m=len(sub)
    i=0
    while i<m:
        h=k*h+ord(sub[i])
        i+=1
    return h
def rabin (txt,pttrn):
    k=4
    m=4
    h=hash(pttrn,k)%101
    a=[0]*(4**3*4**4)
    i=0
    while i<(len(txt)-m+1):
        t=hash(txt[i:i+m],k)
        a.insert(t%101,i)
        i+=1
    j=0
    while j<m:
        if pttrn[j]==txt[(a[h]+j)]:
            j+=1
        else:
              return "not found"
    return print(a[h])

              
 
