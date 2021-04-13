
def codon_format_1(sequence_list):
	codons = []
	index = 0
	while index < (len(sequence_list)):
		if index == len(sequence_list)-2:
			val = ''.join(sequence_list[index:index+2])
			codons.append(val)
			index = index+2
		elif index == len(sequence_list)-1:
			val = ''.join(sequence_list[index:index+1])
			codons.append(val)
			index = index+1
		else:
			val = ''.join(sequence_list[index:index+3])
			codons.append(val)
			index = index+3
	return codons

def codon_format_2(sequence_list):
	codons = []
	index = 1
	while index <= (len(sequence_list)):
		if index % 3 == 0 and len(''.join(sequence_list[index-3:index])) !=0:
			codon = ''.join(sequence_list[index-3:index])
			codons.append(codon)
		index += 1
	return codons


def codons_check(codons,expected):
	if codons == expected:
		print('Nice job!')
		print(codons)
		print(expected)
	else:
		print('Not Quite')
		print('codons')
		print(codons)
		print(len(codons))
		print('Expected')
		print(expected)
		print(len(expected))

def main():
	seq = 'GATATATGCATATACTAACAACAA'
	expected = ['GAT','ATA','TGC','ATA','TAC','TAA','C']
	expected_complete_codons = ['GAT','ATA','TGC','ATA','TAC','TAA','CAA','CAA']
	seq = list(seq)
	codons_c = codons_format_2(seq)
	codons_check(codons_c,expected_complete_codons)
	
if __name__ == '__main__':
	main()