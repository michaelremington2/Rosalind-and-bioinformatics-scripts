sequence = 'CGACCGACGCGCACGACCGAACGACCGACTCCGACCGATCGACCGAGCCGACCGAGCGACCGAACGACCGACCGACCGACGACCGAATCGACCGATCGACCGAGGCGACCGATCGCACGACCGACCCACTCCGACCGAGACGACCGAATCGACCGAACGACCGAGCGACCGACCGACCGACGACCGAACGACCGACGCGACCGACGACCGACGCAGACGACCGACCGACCGAAGCGACCGAACGACCGAGACCCATAGACGACCGATCTTTGTACGACCGAACTACGACCGACCGACCGACCGACCGACGACCGAGGCCTACCGTCGACCGACGACCGACCGACCGACGACCGAGCGACCGATCGACCGACGACCGACCTAGACGACCGACGACCGACTTTCGACCGACTCCAGGCGGGTGATCTTACGACCGAATTTGCGACCGAAAGGGCCCGACCGACAGGTCTCCGTTAAGACGACCGAGTGAACGACCGATAGCCAGTGCGACCGACACGACCGATCGACCGAACGACCGATCTCGACCGAAAGTCACATCGACCGACGACCGAACAACGCACTCATGCGACCGACCGACCGAGATACGACGTCGACCGACCGACCGACGACCGAACGACCGAGTCCGACCGACGACCGACGACCGACCGTGCGACCGATCCGGGAAACGACCGAACAACTTTGCGGCCGACCGATCGAGGGCACGACCGAGCGACCGACGACCGAACGACCGATGCGACCGAGGACGACCGATTCGTCCGACCGACGACCGACGCGACCGACGACCGACCGACCGAATCTACGACCGACCGACCGACTATCACGACCGACGACCGAGCGACCGAGCGACCGACGACCGAGGATCGACCGATCGAAAGTCCGACCGATTCGACCGACACGACCGACGACCGACGACCGAACGTCTCAAACGACCGACTGCGACCGAGCCCGACCGACGACCGAGCGACCGACGACCGA'
motif_sequence = 'CGACCGACG'

def motif_finder(sequence,motif):
	motif_length = len(motif)
	motif_list = []
	for i in range(len(sequence)):
		sub_sequence = ''.join(sequence[i:i+motif_length])
		if motif == sub_sequence:
			motif_list.append(i+1)
	return motif_list

print(motif_finder(sequence,motif_sequence))