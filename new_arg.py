#!/usr/bin/env python

# writing a python file to interpret arguments i.e from the command line

# The strange name argv stands for “argument values”
# whenever Python runs a program, it takes all of the values
# given on the command line and puts them in the list sys.argv
# so that the program can determine what they were
import sys

print("This is the name of the script: ", sys.argv[0])
print("The name of the first argument is the same: ", sys.argv[0])
print("This is the name of the second argument: ", sys.argv[1])
print("This is the name of the third argument: ", sys.argv[2])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

for x in sys.argv:
    print('Argument: ', x)
