import sys, random, argparse
sys.path.append('../utilities/') #CHANGE THIS PATH IF SCR
import my_utils

parser=argparse.ArgumentParser(
    description="generates a random dataset of sequences")
parser.add_argument("outFile", type=str,
                   help="name of the output file the \
                   generated sequences will be printed to")
parser.add_argument("numSeqs", type=int, 
                    help="number of sequences to create")
parser.add_argument("minLength", type=int,
                   help="minimum sequence length")
parser.add_argument("maxLength", type=int,
                   help="maximum sequence length")
args=parser.parse_args()

outs = open(args.outFile, 'w')
for i in range(args.numSeqs):
    randLen = random.randint(args.minLength, args.maxLength)
    randSeq = my_utils.rand_seq(randLen)
    seqName = "seq" + str(i)
    outs.write(">" + seqName + "\n" + randSeq + "\n")

outs.close()
