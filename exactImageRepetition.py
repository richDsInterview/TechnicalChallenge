#!/usr/bin/env python

"""A simple python script to exactly compare an image to all the images contained in a database
    directory using a naive file-reading approach, and a numpy array-based approach
Arguments:
    infile : path to image file to compare
    dbDir : path to database directory containing comparison images
Returns:
    Truth value echoed to command line
"""
import sys
import argparse
import os
import cv2
import numpy as np

def compareImagesBinary(file1, file2):
    if open(file1, 'rb').read() == open(file2, 'rb').read():
        return True

def compareImagesNumpy(file1, file2):
    return np.array_equal(cv2.imread(file1), cv2.imread(file2))

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")

    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.dbDir)


    binaryMatch = False
    numpyMatch = False

    for dbImg in os.listdir(args.dbDir):
        absImgPath = baseDir + "/" + dbImg
        # test if the input images are EXACTLY the same as any in the database directory
        if compareImagesBinary(args.infile, absImgPath):
            binaryMatch = True

        # test if the numpy representation of the image is the same as any in the database directory
        if compareImagesNumpy(args.infile, absImgPath):
            numpyMatch = True

    # print the result
    print("Exact matching image found in database directory: ",  str(binaryMatch))
    print("Matching numpy representation to input image's found in database directory: ", str(numpyMatch))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))