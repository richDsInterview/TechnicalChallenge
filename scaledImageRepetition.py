#!/usr/bin/env python

"""A simple python script to exactly compare an image to all the images contained in a database
    directory using a naive file-reading approach
Arguments:
    infile : path to image file to compare
    dbDir : path to database directory containing comparison images
Returns:
    Truth value echoed to command line
"""
import sys
import argparse
import os


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")

    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.dbDir)

    # test if the input images are EXACTLY the same as any in the database directory
    match = False
    for dbImg in os.listdir(args.dbDir):
        absImgPath = baseDir + "/" + dbImg
        if open(args.infile, 'r').read() == open(absImgPath, 'r').read():
            match = True

    # print the result
    print "Exact matching image found in database directory: " + str(match)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


def get_num_bits_different(hash1, hash2):
    return bin(hash1 ^ hash2).count('1')