def parse_fasta(fh):
    while True:
        first_line = fh.readline()
        if len(first_line) == 0:
            break 
        first_line[1:]
        seq = fh.readline().rstrip()
    return seq
def parse_fastq(fh):
    while True:
        first_line = fh.readline()
        if len(first_line) == 0:
            break  
        name = first_line[1:]
        seq = fh.readline().rstrip()
        fh.readline()  
        fh.readline()
    return seq
def naive( p,t):
    assert len(t)>=len(p)
    z=0
    y=0
    occurrences = []
    for i in range(0, len(t)-len(p)+1):
        match = True
        for j in range(0, len(p)):
            if t[i+j] != p[j]:
                match = False
                z=z+1
                break
        if match:
            y=y+1
            occurrences.append((i))
    occurrences.append(z)
    occurrences.append(y)
    return occurrences
if __name__ == '__main__':
  fname=input("please enter yr fasta file :")
  f = open(fname, 'r')
  p=input("please enter your pattern :")
  if fname[-1]=="a":
     t=parse_fasta(f)
  elif fname[-1]=="q":
     t=parse_fastq(f)
  occurrences = []
  occurrences = naive(p,t)
  print("success times:" +str(occurrences[-1]))
  print("failed times:" +str(occurrences[-2]))
  print("occurrences places:" +str(occurrences[:-2]))
  f.close()

