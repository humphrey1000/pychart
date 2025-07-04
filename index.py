import re


def parser(regexp, prose):
    """ \
            Parsing data
        Data types: variables, functions, data structures, operators, classes
    """
    text = re.findall(regexp, prose)
    print(text)


# if __name__ == '__main__':
#     text = sys.argv[1], sys.argv[2]
#     parser(*text)

well = "hello", "howdy means how do ye, anyway hello"
parser(*well)
