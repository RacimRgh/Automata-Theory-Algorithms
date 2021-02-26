#
#   Python DFA
#
from Graph import *
from Parser import *
from Algorithms import *


def main():
    # get filename to open
    uInput = "abab.txt"
    try:
        file = open(uInput)
    except:
        print("Invalid file")

    # parse file and get alphabet, nodes, and final states
    fileParser = Parser(file)
    fileParser.parse()

    algorithms = Algorithms(fileParser)


if __name__ == '__main__':
    main()
