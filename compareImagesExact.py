#!/usr/bin/env python

"""A simple python script to exactly compare two images
Returns: Truth value
"""
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile1', help="Input file 1", type=argparse.FileType('r'))
    parser.add_argument('infile2', help="Input file 2", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)

    # test if the input images are EXACTLY the same
    print args.infile1.read() == args.infile2.read()
    return args.infile1.read() == args.infile2.read()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))