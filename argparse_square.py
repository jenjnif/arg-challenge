import argparse

parser = argparse.ArgumentParser()

# by default argparse treats the options given as a string
# but using type=int will treat the input as an integer
parser.add_argument("square", help="display square of"
                    + " a given number", type=int)
parser.parse_args()
args = parser.parse_args()
print(args.square**2)
