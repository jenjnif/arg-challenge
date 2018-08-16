#!/usr/bin/env python

# writing a python file to interpret arguments i.e from the command line

import sys

print("This is the name of the script: ", sys.argv[0])
print("The name of the first argument is the same: ", sys.argv[0])
print("This is the name of the second argument: ", sys.argv[1])
print("This is the name of the third argument: ", sys.argv[2])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

for x in sys.argv:
    print('Argument: ', x)
