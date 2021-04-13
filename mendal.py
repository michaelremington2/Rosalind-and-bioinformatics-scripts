
def dom_allele_prob(pop_AA,pop_Aa,pop_aa):
	'''Returns probability of having a dominant child'''

	t = pop_AA+pop_Aa+pop_aa
	t_min_1 = t-1
	AA_AA = pop_AA*(pop_AA-1) # only AA _children
	AA_Aa = (pop_AA*pop_Aa)*2 #Aa_AA and AA_Aa
	Aa_Aa = pop_Aa*(pop_Aa-1)*.75
	aa_Aa = pop_aa*pop_Aa*.5*2 # aa_Aa and Aa_aa
	AA_aa = pop_AA*pop_aa*2
	aa_aa = pop_aa*(pop_aa-1)*0
	halotype_set = [AA_AA,AA_Aa,Aa_Aa,aa_Aa,AA_aa,aa_aa]
	return sum(halotype_set)/(t*t_min_1)



if __name__ == "__main__":
	AA=29
	Aa=25 
	aa=23
	blah = dom_allele_prob(AA,Aa,aa)
	print(blah)












    


