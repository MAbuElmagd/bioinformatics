def parse_fastq(fh):
    """ Parse reads from a FASTQ filehandle.  For each read, we
        return a name, nucleotide-string, quality-string triple. """
    reads = []
    while True:
        first_line = fh.readline()#it reads seq id only
        if len(first_line) == 0:
            break  # end of file
        name = first_line[1:].rstrip()#remove @ and whitespaces
        seq = fh.readline().rstrip()#read the next line (seq itself)
        fh.readline()  # ignore line starting with +
        qual = fh.readline().rstrip()
        reads.append((name, seq, qual))
    return reads


if __name__ == '__main__':
  fname=input("please enter yr fasta file :")
  f = open(fname, 'r')
  reads = []
  reads=parse_fastq(f)
  print(reads[1])
  #print(reads)
  f.close()

