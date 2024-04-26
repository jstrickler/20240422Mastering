import sys
import re
import fileinput
from argparse import ArgumentParser

parser = ArgumentParser(description="Faux grep")
parser.add_argument("-f", dest="show_filename", action="store_true", help="Show file name")
parser.add_argument("-i", dest="ignore_case", action="store_true", help="Ignore case")
parser.add_argument("pattern", help="RE Pattern to find")
parser.add_argument("files", nargs="*", help="file(s) to search")

args = parser.parse_args()   # parses sys.argv

#               OPTIONS TERM       FILES ...
#  file_input.py -f -i search-term file1 file2 file3 ...

# fileinput.input() is an iterator of all lines 
# in all files in sys.argv[1:]

regex = re.compile(args.pattern, re.IGNORECASE if args.ignore_case else 0)

for raw_line in fileinput.input(args.files):  
    if regex.search(raw_line):
        if args.show_filename:
            print(fileinput.filename(), end=" ")
        print(raw_line.rstrip())
