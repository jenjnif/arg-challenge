# writing a python file to interpret arguments i.e from the command line
# including an argument that squares an int input

import sys


if len(sys.argv) == 1:
    print('usage: ' + sys.argv[0] + ' [-h] square\n' +
          sys.argv[0] + ': error: the following arguments' +
          ' are required: square')

if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print('usage: ' + sys.argv[0] + ' [-h] square\n\n' +
              'positional arguments:\n' + '  square      ' +
              'display square of a given number\n\n' +
              'optional arguments:\n' + '  -h, --help  show' +
              ' this help message and exit')
    else:
        try:
            number = int(sys.argv[1])
            print(number**2)
        except ValueError:
            print('usage: ' + sys.argv[0] + ' [-h] square\n' +
                  sys.argv[0] + ': error: argument square: invalid' +
                  ' int value: ' + "'" + sys.argv[1] + "'")
