class bioinformatics_exploratory_analysis:
    def __init__(self,dna_sequence):
        self.dna_sequence = dna_sequence
        self.dna_sequence_list = list(dna_sequence)
        self.a_count = 0 
        self.t_count = 0
        self.g_count = 0
        self.c_count = 0
        self.dna_nucleotide_count = self.nucleotide_count()
        self.gc_content = self.gc_content_calc() 
        self.acceptable_dna_nucloetides = ['A','T','C','G']
        self.rna_sequence = self.dna_to_rna()
        #self.complementary_strand = self.dna_reverse_complement_string()

    def individual_nucleotide_display(self):
        '''Sample sequence is a list of nucleotides'''
        for i in range(0,len(self.dna_sequence)):
            if self.dna_sequence[i] not in self.acceptable_dna_nucloetides:
                print('Error, fix  '+ self.dna_sequence[i] + ' at position ' + str(i))
                break
            else:
                print(self.dna_sequence[i] + ' ' + str(i))

    def dna_sequence_check(self):
        '''Function that checks if a inserted sequence is acceptable to work with. '''
        self.error_list = []
        for i in range(0,len(self.dna_sequence)):
            if self.dna_sequence[i] not in self.acceptable_dna_nucloetides:
                self.error_list.append('Nucleotide Error, fix  '+ self.dna_sequence[i] + ' at position ' + str(i))
            elif self.dna_sequence[i].islower == False:
                self.error_list.append('Case Error ' + self.dna_sequence[i] + ' ' + str(i))
        if len(self.error_list) == 0:
            print('Good Sequence')
        else:
            print(self.error_list)

    def nucleotide_count(self):
        ''' Counts DNA nucleotides'''
        try:
            for i in range(0,len(self.dna_sequence)):
                if self.dna_sequence[i] == 'A':
                    self.a_count += 1
                elif self.dna_sequence[i] == 'T':
                    self.t_count += 1
                elif self.dna_sequence[i] == 'G':
                    self.g_count += 1
                elif self.dna_sequence[i] == 'C':
                    self.c_count += 1
        except ZeroDivisionError:
            pass

    def gc_content_calc(self, decimals = 4):
        '''Calculates the GC content ratio. this ratio is the sum of guanines and cytosines over the total count of nucleotides.'''
        try:
            return round(((self.g_count+self.c_count)/(self.g_count+self.c_count+self.a_count+self.t_count)), decimals)
        except ZeroDivisionError:
            print('Zero Divison Error')

    def dna_to_rna(self):
        '''Returns the complementaRY rna sequence of a dna sequence.'''
        return self.dna_sequence.replace("T", "U")
    
    def complementing_nucleotide(self):
        self.complementary_strand = []
        for item in reversed(self.dna_sequence_list):
            if item == 'A':
                self.complementary_strand.append('T')
            elif item == 'T':
                self.complementary_strand.append('A')
            elif item == 'G':
                self.complementary_strand.append('C')
            elif item == 'C':
                self.complementary_strand.append('G')
            else:
                print('error complementary strand')
                break
        return  ''.join(self.complementary_strand)

def fullstring_string_cleaning():
    with open('fastapractice.txt', 'r') as f:
        sample_sequence1 = f.read()
        import re
        sample_sequence1 = re.sub('[>]Rosalind_\d\d\d\d' , '', sample_sequence1, flags=re.MULTILINE)
        sequence = []
        for line in sample_sequence1.split('\n'):
            if len(line)>1:
                line = line.replace('\n','')
                sequence.append(line)
        clean_sequence = ''.join(sequence)
    return clean_sequence

def sequence_split():
    with open('fastapractice.txt', 'r') as f:
        sample_sequence1 = f.read()
        import re
        sample_sequence1 = re.compile('[>]' ).split(sample_sequence1)
        seq = []
        for line in sample_sequence1:
            if len(line)>1:
                seq.append(line)
        return seq


if __name__ ==  "__main__":
    pass

        
