def gc(seq):
    gcCount = seq.count("C") + seq.count("G")
    gcFrac = float(gcCount) / len(seq)
    
    return round(gcFrac,2)

def rand_seq(length):
    import random
    
    nts = ['A','C','G','T']
    seq = ""
    for i in range(length):
        seq += random.choice(nts)
    
    return seq

def shuffle_nt(seq):
    import random
    
    strList = list(seq)
    random.shuffle(strList)
    shuffSeq = "".join(strList)
    
    return shuffSeq

def reverse_compl(seq):
    complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    compl = ""
    for char in seq:
        compl = complements[char] + compl
    
    return compl

def read_fasta(fileName):
    ins = open(fileName, 'r')
    seqDict = {}
    activeID = ""

    for line in ins:
        line = line.rstrip('\r\n')
        
        if line[0] == ">":
            activeID = line[1:] 
            if activeID in seqDict:
                print (">>> Warning: repeat id:", activeID, "-- overwriting previous ID.")
            seqDict[activeID] = ""
            
        else:
            seqDict[activeID] += line 
    
    ins.close()    
    
    return seqDict
