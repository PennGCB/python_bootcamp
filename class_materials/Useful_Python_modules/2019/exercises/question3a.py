import sys, os, argparse

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
    
if not os.path.exists(args.outputFolder):
    print ("Creating output folder (%s)"
           % args.outputFolder)
    os.mkdir(args.outputFolder)
