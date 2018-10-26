def make_bad_match_table(pattern):

    length = len(pattern)
    table = {}
    for i, c in enumerate(pattern):
        if i == length-1 and not c in table:#last char = length
            table[c] = length
        else:
            table[c] = length - i - 1

    return table


def boyer_moore(pattern, text):

    match_table = []
    pattern_length = len(pattern)
    text_length = len(text)
    assert  pattern_length <= text_length

    table = make_bad_match_table(pattern)
    index = pattern_length - 1
    pattern_index = pattern_length - 1

    while index < text_length:
        if pattern[pattern_index] == text[index]:
            if pattern_index == 0:
                match_table.append(index)
                pattern_index = pattern_length - 1
                index += (pattern_length * 2 - 1)
                #print(index)
               
            else:
                pattern_index -= 1
                index -= 1
        else:
             #get the number of skips 
             #if not exist will return length ( * >> any char)
            index += table.get(text[index], pattern_length)
            pattern_index = pattern_length - 1

    return match_table

if __name__ == '__main__':
    with open ("DRR001336.fastq","r") as f:
         f.readline()
         target=f.readline().rstrip()
         f.readline()
         f.readline()
    pattern="CCT"
    with open ("boyermoore.txt","w") as report:
         print(boyer_moore(pattern,target),file=report)
    f.close()
    report.close()
