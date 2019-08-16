import argparse

parser=argparse.ArgumentParser()
parser.add_argument("var1")
parser.add_argument("var2")
parser.add_argument("var3")
parser.add_argument("var4")
args=parser.parse_args()

print(args.var1)
print(args.var2)
print(args.var3)
print(args.var4)

