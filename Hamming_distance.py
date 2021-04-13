s = 'TTACTGTGGCCTTTAGTACAAGTCTACTTGCTAGTACTCATATCCTACGCCCGAGTGTAATTAATTCGAGCTCGGTAGAACGGGCGATTGTTACAACACCTCCGTCTCGAACATATAGTACCCTCTGGAAGTTTCGGGAACCAACCCCGACGGAGTCCTTGATGGCGTTGTCGTCGCTGATGTCCTTAAGGTGGCACGAATGGTCTAGGCAGCAATAATCGAGACAAGCAAGTCTCAATGGCATTGACTTGAAGCTACTAGGGGTTTTAAGCCGAGGGTCTCGTTCATGTTGAAGCGACCACCTCGGCATTTGCACTATCTCGTCCTGTCGGCCACGTGTCACCGTAAGCCGGCAGGCATGACCTCTCATAGGGGACAGGGATAAAACCGGAAGAATGGCTGGTTCATACTAGCGTTGGATCTAAGACGGTACTTAAATCTTGCGGCGTCTAGCGGGTCCCATATGCTCGTGTTGTAGCGGTTAAGAGTATTTGAGAATCCGGTCAGGCCCTGTAGATGAATGCATCGAATCATATCCGAAAGAACTTTTAGCGAGCAAAAGACGGCTTCCCCTAGCTTGGAACTGACACTCCAGCCGGACCCACACAGGGCAATATGCAAAATACTTGGAGTTGGTTACATCCTTGACGAACAAACATATGTTTCTACGTCTGAGTCACAGTATTTTGCCGTATGTAGCACCGAATGGCTCGTGGAGTAAGGGTTACCAGCCGTCTGCAGAAGGAGTCATGTAACTTAGGAGACATTACACAGTGGAGTGAGCAGAGAAAGACATTTGACGTGTAATCTCAAGGCTTTGACGCCACTATCGAGCATACGCTCTCCGGTGTCCGCGTCTGACGGGCGACCTACACTGATGTCCCAGGTCACTGTGATGAACTCGAGCACCTATATAGGATACTGAAGCTTACGAGTTGGGGAGTCATATGATCGACTAGCTA'
t = 'TGCATGCCATCTTTGGTACGAGTCGGCTTTCTAGTAGTACTAGTTGATGCCCGCGTCCGCATCCATGAGACGACGATGATCGGGGGTTTGGCAGGACCGATCCTTCCGCTAGTCGGCTCATAGTTTCTAAGATGCAGGAAACGTGAACGAACAGGCCCCAGATCGCGCCGGTAACATACATGACAATAACGGAGCGGTCATGTTCCACGCCGCAATGACTCAGGAGATCACTTAACGATGGCGTTGTCGATAAGCTCTATGCGCTATTAAGCGGAGTCTCTAGCCCGTCCGATGGGGATAAATGCCGCACTTTTACACCATCGTCCGATCGTCCACATCCCACCGGAAGTTAGCAGGGATGACCTGCAAATGGTCACGACACTACCATCGACCGCAGCTTCGAGTGATCCCAGGCATCATCCTGAGCAAGTCCTAGTATCCTGAGGGGCAACGGCGGATCATGATGGTAAGGCGCCATGGGCAGATACATATTACAAACCCGGTAAGGAACTGGTGTGTAATCCAATTAGTCCGCTCGAGACGATTTATCTGGCGGGAGAAGGAGCCTTACCTAAGCCGCCATAAGCCCGCTCACCTGCACGGTCGCAAGGGCATGTGGAAGGTACCCGCATGTTTCGTCATCCAATGACGTACCAACCCTGTTCTTAGGTCAGAGACAACGAATTACACCCTCTTTCACACCCTAAGTACTACTCTGTCGAGCTTACGTGACGCCTGGAGCACTAGTCGTATAATTTCGGACGCATTGCGCTTTGAATGAGTCCCTTAAAATGCGTAGACTTCTGTTGTTAAGGCTTTATCCTCACTTGGGATCAGCCCATTTCAGATGTACCACTGTGATGGAAGAGGTAAGCTGTGGAGCCAGGTCCATGGGACGAAGACGATTACAAGTCTTGGATACTTAGAATTAAGAGCAGGGAACTCCTTTTCTACTTTGGATG'

def hamming_distance(sequence1,sequence2):
    dict1=dict(enumerate(list(sequence1)))
    dict2=dict(enumerate(list(sequence2)))
    if len(sequence1) != len(sequence2):
        return 'Mismatch string length'
    else:
        n=0 
        for key1,value1 in dict1.items():
            for key2,value2 in dict2.items():
                if value1 != value2 and key1 == key2:
                    n=n+1
        return n

print(hamming_distance(s,t))

def better_hamming_distance(seq1,seq2):
    '''Zip Makes a list of tuples '''
    return [ a!=b for (a, b) in zip(seq1, seq2)].count(True)

print(better_hamming_distance(s,t))