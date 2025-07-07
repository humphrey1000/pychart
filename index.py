import re
import sys


def parser(regexp, prose):
    """ \
            Parsing data
        Data types: variables, functions, data structures, operators, classes
    """
    text = re.findall(regexp, prose)
    print(text)


if __name__ == '__main__':
    are = sys.argv[1], sys.argv[2]
    parser(*are)

# well = r'hello', "howdy means how do ye, anyway hello"
# parser(*well)
