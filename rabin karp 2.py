def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
 
    # The value of h would be "pow(d, M-1)%q" h=(K^M-1)
    for i in range(M-1):
        h = (h*k)%q
        
 
    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (k*p + ord(pat[i]))%q
        
        t = (k*t + ord(txt[i]))%q
        print(t)
 
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
 
            j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                print ("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (t-h*ord(txt[i]))%q # remove letter i
            #print(t)
            t=t*k
            t = (t+ord(txt[i+M]))%q # add letter i+M
            t = (t+q)%q # make sure that t >= 0
 


if __name__ == '__main__':
     txt = "ATTCCGT"
     pat = "TCCG"
     k=4
     q = 11 # A prime number
     print(search(pat,txt,q))
