acceptable_nucloetides = ['A','T','C','G']


def rosalind_nucleotide_count(sample_sequence):
    acceptable_nucloetides = ['A','T','C','G']
    As = 0 
    Ts = 0 
    Gs = 0 
    Cs = 0 
    for i in range(0,len(sample_sequence)):
        if sample_sequence[i] in acceptable_nucloetides:
            if sample_sequence[i] == 'A':
                As += 1
            elif sample_sequence[i] == 'T':
                Ts += 1
            elif sample_sequence[i] == 'G':
                Gs += 1
            elif sample_sequence[i] == 'C':
                Cs += 1
            else:
                print('error')
                break
    #gc = gc_content(As,Ts,Gs,Cs)
    return As,Ts,Gs,Cs

def gc_content(sample_sequence, decimals = 6):
    As,Ts,Gs,Cs = rosalind_nucleotide_count(sample_sequence)
    return round(((Gs+Cs)/(As+Ts+Gs+Cs)) * 100, decimals)

def main(file_name):
    import collections as c
    seq_dict = {}
    fastalabel = ''
    with open(file_name) as fh:
        seq = fh.readlines()
        for line in seq:
            line = line.strip()
            line = line.strip('\n')
            if line.startswith('>'):
                fastalabel = line
                seq_dict[fastalabel] = ''
            else:
                seq_dict[fastalabel] += line
    gc_dict = {key: gc_content(value) for (key,value) in seq_dict.items()}
    max_key = max(gc_dict,key=gc_dict.get)
    end_result = f'{max_key}\n{gc_dict[max_key]}'.strip('>')
    print(end_result)

if __name__ ==  "__main__":
    main('rosalind_gc.txt')