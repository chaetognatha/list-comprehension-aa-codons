"""
This was adapted from an incredibly elegant list comprehension found on http://www.petercollingridge.co.uk/tutorials/bioinformatics/codon-table/
I wanted to see if I could adapt it to list codons given the amino acid, and it worked.
"""
nts = "tcag" #nucleotides in genetic code
cods = [a + b + c for a in nts for b in nts for c in nts] #generates a list of all possible three letter combinations from nucleotides
aas = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG' #string to assigne amino acids to nucleotides
cods_tabl = dict(zip(cods, aas)) # make a dictionary from codons and amino acids
leu = ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'] # hard coded list of codons for L for comparison
print("the correct answer should be: ", "\n", leu) 
rel = [(key, value) for (key, value) in cods_tabl.items() if 'L' in value] #extract all key-value pairs corresponding to string
answer = []
for z, y in rel:
    answer.append(z) #put all requested codons in answer
if answer == leu: #test if the answer is correct
    print(answer, "\n", "yay you did it!!!")
