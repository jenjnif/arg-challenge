import argparse

parser = argparse.ArgumentParser()

# To specify which command-line options the program
# will accept, use the "add_argument()" method.
# In this case I am calling the argument 'echo'
# and echo is a postiional argument:
#     parser.add_argument("echo")
# to get more help about the positional argument (echo)
# I need to change the script slightly
parser.add_argument("echo", help="echo the string you use here")
parser.parse_args()

# running this programme without arguments displays nothing to stdout
# running it with the help option:
#     python3 argparse.py -h
# returns the help message

# this returns data from the options specified (echo)
args = parser.parse_args()
print(args.echo)
