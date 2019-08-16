import sys, os, argparse
sys.path.append('../utilities/') #CHANGE THIS PATH IF SCR
import my_utils

parser=argparse.ArgumentParser(
    description="check file existance")
parser.add_argument("inputFile", type=str,
                   help="an input file name")
parser.add_argument("outputFolder", type=str, 
                    help="output folder name")
args=parser.parse_args()

# check if input file / output directory exist
if not os.path.exists(args.inputFile):
    err_msg = (">>Error: input file (%s) does not exist. Exiting." 
        % args.inputFile)
    sys.exit(err_msg)
    
# if output directory does not exist
# create output directory
if not os.path.exists(args.outputFolder):
    print ("Creating output folder (%s)"
           % args.outputFolder)
    os.mkdir(args.outputFolder)
    
# read in sequences from fasta file & print to separate output files
# you'll get an error for one of them because there's a ">" in the sequence id,
# which is not allowed in a file name. you can handle this however you want.
# here I used a try-except statement and just skipped the problematic file (with a warning message)
seqs = my_utils.read_fasta(args.inputFile)
for seqID in seqs:
    outFile = ("%s/%s.fasta" % (args.outputFolder, seqID))
    outStr = (">%s\n%s\n" % (seqID, seqs[seqID]))
    
    try:
        outs = open(outFile, 'w')
        outs.write(outStr)
        outs.close()
    except IOError:
        sys.stderr.write(">>Warning: Could not print (%s) file. Skipping." % outFile)
    
