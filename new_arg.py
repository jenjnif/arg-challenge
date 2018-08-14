# creating a new argument for the command line not using argparse
# use module one, module two and module three

import sys
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))
