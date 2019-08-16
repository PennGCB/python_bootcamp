'''PART1'''

#open file
seq_file = open("/Users/modia/Downloads/Homo_sapiens_sequence.fa","r")

#make/initialize three lists to capture the sequence of the cDNA, 3'UTR, and 5'UTR

cdna = ""
utr3 = ""
utr5 = ""

#read first line and do nothing with it because its just the name 
seq_file.readline()

#initialize string to save the cDNA 

seq_string = ""

#initialize a count do that you know which of the three sequences you are on 
count = 0 

for lines in seq_file.readlines():
	#print(lines)
	lines = lines.strip()
	#conditional: add lines to cDNA string until you see another sequence type 
	if lines[0]!=">":
		seq_string = seq_string+lines
		#print(seq_string)
	else:
		if count ==0:
			cdna = seq_string
			#print(seq_string)
			seq_string = ""
			count= count+1
		elif count ==1:
			utr3 = seq_string
			#print(seq_string)
			seq_string = ""
			count= count+1

utr5 = seq_string



print(cdna+"\n")
print(utr3+"\n")
print(utr5+"\n")


#close file
seq_file.close()

'''PART2'''

# design primers from the 3'UTR and 5'UTR sequences 
# output a list of primers that should work with the following criteria and make sure to reverse complement the reverse primer


#1. Length of 20 bases
#2. Start and end with 1-2 G/C pairs
#3. 40-60% G/C content - make this a function 

#GC content function - where input is a string sequence:

def gc_content(sequence):
	count = 0
	for base in sequence:
		if base =="G" or base == "C":
			count = count+1
	content = float(count)/len(sequence)
	return (content)



#Starting with the 5'UTR sequence, make a list of all possible 20 base sequences

#initialize list of possible primers 
utr5_primer = []

count =0
for pos in range(0,len(utr5)):
	#print(pos)
	#print(utr5[pos:pos+20])

	primer = utr5[pos:pos+20]

	

	# determine if the primer starts with the following: GG, GC, CC, or CG
	if primer[0:2] == "GG" or primer[0:2] == "GC" or primer[0:2] == "CC" or primer[0:2] == "CG":
		# determine if the primer ends with the following: GG, GC, CC, or CG
		if primer[-2:] == "GG" or primer[-2:] == "GC" or primer[-2:] == "CC" or primer[-2:] == "CG":
			#print(primer)
			#for all passing primers determine their GC content:
			if gc_content(primer) >= 0.4 and gc_content(primer) <= 0.6:
				# for any primer that passes - add to the list of UTR'3 primers
					utr5_primer.append(primer)

print(utr5_primer) #Students should get the following 5 primers as their answer 
['CCTTCTTCTGGTCAGAAACC', 'GGAGAACTAAAAGTATGAGC', 'GCTATGCAGTTTGAATATCC', 'GGCTTACCTCAAATAAATGG', 'GCTTACCTCAAATAAATGGC']

def reverse_complement(sequence):
	complement = ""
	for base in sequence:
		if base == "A":
			complement = complement+"T"
		elif base == "G":
			complement = complement+"C"	
		elif base == "C":
			complement = complement+"G"
		elif base == "T":
			complement = complement+"A"
	#google the reverse shortcut
	reverse_comp = complement[::-1]
	return(reverse_comp)

# do the same thing for the 3'utr sequence but students should output the primers as reverse complemented - they should have a function to do this

#initialize list of possible primers 
utr3_primer = []

count =0
for pos in range(0,len(utr3)):
	#print(pos)
	#print(utr3[pos:pos+20])

	primer = utr3[pos:pos+20]

	

	# determine if the primer starts with the following: GG, GC, CC, or CG
	if primer[0:2] == "GG" or primer[0:2] == "GC" or primer[0:2] == "CC" or primer[0:2] == "CG":
		# determine if the primer ends with the following: GG, GC, CC, or CG
		if primer[-2:] == "GG" or primer[-2:] == "GC" or primer[-2:] == "CC" or primer[-2:] == "CG":
			#print(primer)
			#for all passing primers determine their GC content:
			if gc_content(primer) >= 0.4 and gc_content(primer) <= 0.6:
				# for any primer that passes - add to the list of UTR'3 primers
					#print(primer)
					#print(reverse_complement(primer))
					utr3_primer.append(reverse_complement(primer))

print(utr3_primer) #Students should get the following 2 primers as their answer 

#5'3': ["CCCAATAAATATAGGACTGG","CCAGTCCTATATTTATTGGG"]

#Reverse-complemented: ['CCAGTCCTATATTTATTGGG', 'GCCTCAGACATCTCCAGTCC']



'''PART3 - for next week after they learn dictionaries'''

#Convert your cDNA sequence into its amino acid sequence. 
# Note your first codon should start with ATG - so you must go through the whole cDNA sequence to find all possible start sites.
# Consider all three 5'3 frames - if you don't know what this means ask a TA 





