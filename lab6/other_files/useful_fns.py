# Count (potentially overlapping) 
#  instances of a subsequence in 
#  a string
def count_occurrences(seq, subseq):
	seq = seq.upper()
	subseq = subseq.upper()
	count = 0
	index = 0
	done = False
	while not done:
		index = seq.find(subseq, index)
		if (index == -1):
			done = True
		else:  
			count += 1
			index += 1 
	return count
