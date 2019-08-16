import argparse, sys

parser=argparse.ArgumentParser(
    description="return the quadratic formula")
parser.add_argument("a", type=float)
parser.add_argument("b", type=float)
parser.add_argument("c", type=float)
args=parser.parse_args()

a = args.a
b = args.b
c = args.c
underRoot = (b**2 - 4*a*c)
if underRoot >= 0:
    x1 = ( (-b) + underRoot ** 0.5 ) / float(2*a)
    x2 = ( (-b) - underRoot ** 0.5 ) / float(2*a)
    x1 = round(x1,3)
    x2 = round(x2,3)
    sys.stdout.write("x = {x1} or {x2}\n".format(x1=x1,x2=x2))
else:
    sys.exit("ERROR: non-real answer. Exiting.")
