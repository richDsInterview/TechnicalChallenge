#!/usr/bin/env python

"""A simple python script to exactly compare two images
Returns: Truth value
"""
import sys
import argparse
import os


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('db_dir', help="'Database' directory")

    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.db_dir)

    # test if the input images are EXACTLY the same as any in the database directory
    match = False
    for dbImg in os.listdir(args.db_dir):
        absImgPath = baseDir + "/" + dbImg
        if open(args.infile, 'r').read() == open(absImgPath, 'r').read():
            match = True

    # print the result
    print "Exact matching image found in database directory: " + str(match)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))