def naive(p, t):
'''assert statment ::
  you're telling the program to test that condition,and trigger an error
    if the condition is false.
    In Python, it's roughly equivalent to this:

if not condition:
    raise AssertionError()
    Python’s assert statement is a debugging aid, not a mechanism for
    handling run-time errors(try&catch)
    asserts are useful to check conditions that should be true in a
    given position of your code(usually, the beginning (preconditions)
    and the end of a function (postconditions)).'''
    assert len(p) <= len(t)
    
    occurrences = []
    for i in range(0, len(t)-len(p)+1):
        match = True  
        for j in range(0, len(p)): #for the pattern
            if t[i+j] != p[j]:
                match = False 
                break
        if match:
            occurrences.append(i)
    return occurrences

if __name__ == '__main__':
 t="CTTCTGTCTGGGTCT"
 #t="CTTCTG"
 p="TCT"
 occurrences = []
 occurrences = naive(p, t)
 print(occurrences)
 i=occurrences[0]
 j=i+len(p)
 print(t[i:j])

'''for i in range(0, len(occurrences)):
    x=occurrences[i]
    y=x+len(p)
    print(x)
    print(t[x:y])'''
