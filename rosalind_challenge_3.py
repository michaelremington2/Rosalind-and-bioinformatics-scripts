#import os
#print(os.getcwd())
#os.path.exists(Data_Files)

def data_pop():
    directory = '/home/mike/Documents/python-practice-projects/rosalind-challenge/michael/Data_files/practice.txt'
    with open(directory) as f:
        sequence = f.read()
        sequence = sequence.upper()
        sequence = sequence.strip()
        sequence = sequence.replace('\n','')
    return sequence




def complementing_nucleotide(dna_sequence):
    dna_sequence_list = list(dna_sequence)
    complementary_strand = []
    for item in reversed(dna_sequence_list):
        if item == 'A':
            complementary_strand.append('T')
        elif item == 'T':
            complementary_strand.append('A')
        elif item == 'G':
            complementary_strand.append('C')
        elif item == 'C':
            complementary_strand.append('G')
    return  ''.join(complementary_strand)

sequence= data_pop()
#sequence ='AACGCTAAAGGGTCCA'
reversered_sequence = complementing_nucleotide(sequence)
leading_strand = "5' {} 3'".format(sequence)
lagging_strand = "3' {} 5'".format(reversered_sequence)
print(leading_strand)
print(lagging_strand)
print(len(sequence))
print(len(reversered_sequence))