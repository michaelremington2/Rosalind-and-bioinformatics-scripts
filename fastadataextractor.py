class fastaDataExtractor:
	def __init__(self,fasta_file_name):
		self.file_name = fasta_file_name
		self.fasta_dict = {}
		self.file_check()
		self.list_clean()
		self.file_to_dict()
		self.dna_2_rna()

	def file_check(self):
		''' checks if the file is a fasta file and if it is not it raises an error'''
		x=self.file_name.split('.')
		if x[1] != 'fasta':
			raise ValueError('Input fasta file type.')

	def open_file(self):
		'''opens the .fasta file of and makes each line into a list'''
		with open(self.file_name) as f:
			i = f.readlines()
		return i

	def list_clean(self):
		'''Cleans strings in rna to protein matching list'''
		lib = self.open_file()
		clean_lib = []
		for line in lib:
			line = line.replace('\n','')
			line = line.strip()
			if line.startswith('>'):
				clean_lib.append(line)
			else:
				line = line.upper()
				for i in line:
					clean_lib.append(i)
		self.fasta_list = clean_lib

	def codon_formatter(self,sequence_list):
		'''Function takes a list of nucleotides and formats them into codons.'''
		codons = []
		index = 1
		while index <= (len(sequence_list)):
			if index % 3 == 0 and len(''.join(sequence_list[index-3:index])) !=0:
				codon = ''.join(sequence_list[index-3:index])
				codons.append(codon)
			index += 1
		return codons

	def file_to_dict(self):
		'''Generates a basic dictionary of the fasta discription as the key and the block sequence as the items.'''
		fastalabel = ''
		for x in self.fasta_list:
			if x.startswith('>'):
				fastalabel = x
				self.fasta_dict[fastalabel] = ''
			else:
				self.fasta_dict[fastalabel] += x
	def dna_codon_dict(self):
		'''Makes a dictionary where the key is the fasta description and the items are a list of codons.'''
		self.fasta_codon_dict = {key: self.codon_formatter(value) for key,value in self.fasta_dict.items()}
	
	def dna_nucleotide_dict(self):
		'''Makes a dictionary where the key is the fasta description and the items are a list of nucleotides.'''	
		self.fasta_nucleotide_dict = {key: list(value) for key,value in self.fasta_dict.items()}

	def dna_2_rna(self):
		'''This still needs some work, I forgot to implement transcription'''
		self.rna_codons = {}
		for key,value in self.fasta_codon_dict.items():
			temp_list =[]
			for i in value:
				val = i.replace('T','U')
				temp_list.append(val)
			self.rna_codons[key]= temp_list
		

def main():
	import sys
	#file_name = 'usacovidsequence.fasta'
	file_name = sys.argv[1]
	a = fastaDataExtractor(file_name)
	print(a.rna_codons)

if __name__ == '__main__':
	main()    


