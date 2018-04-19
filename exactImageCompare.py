#!/usr/bin/env python

"""A simple python script to exactly compare two images
"""

#from __future__ import print_function
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile1', help="Input file 1", type=argparse.FileType('r'))
    parser.add_argument('infile2', help="Input file 2", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))