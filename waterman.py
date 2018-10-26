

import numpy as np

match = 5
mismatch = -2
gap = -3

def match_score(c1, c2):
    if c1 == c2:
        return match
    elif c1 == '-' or c2 == '-':
        return gap
    else:
        return mismatch

def needle(seq1, seq2):
    m, n = len(seq1), len(seq2)
    score = np.zeros((m+1, n+1),dtype=int)
    ma=0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            diagnal = score[i-1][j-1] + match_score(seq1[i-1], seq2[j-1])
            up = score[i-1][j] + gap
            left = score[i][j-1] + gap
            if max(diagnal, up, left)<=0:
                continue
            else:
                score[i][j] = max(diagnal, up, left)
            if ma<score[i][j]:
                ma=score[i][j]
                x,z=i,j
    print(score)
    align1, align2 = '', ''
   
    while score[x][z]!=0:
        score_current = score[x][z]
        score_diagnal = score[x-1][z-1]
        score_left = score[x][z-1]
        score_up = score[x-1][z]
        
       

        if score_current == score_diagnal + match_score(seq1[x-1], seq2[z-1]):
            
            a1,a2 = seq1[x-1],seq2[z-1]
            x,z = x-1,z-1
        elif score_current == score_up + gap:
            
            a1,a2 = seq1[x-1],'-'
            i -= 1
        elif score_current == score_left + gap:
           
            a1,a2 = '-',seq2[z-1]
            j -= 1
        
        align1 += a1
        align2 += a2
    while x > 0 and score[x][z]!=0 :
         a1,a2 = seq1[x-1],'-'
         align1 += a1
         align2 += a2
         x -= 1
        
    while z > 0 and score[x][z]!=0 :
        a1,a2 = '-',seq2[z-1]
        
        align1 += a1
        align2 += a2
        z -= 1   

    
    
    align1 = align1[::-1]
    align2 = align2[::-1]
    
  
    print (score)  
    print("score= " + str(score[m,n]))
    print(align1)
    print(align2)

if __name__ == '__main__':
    needle("GGA","TGAC")
