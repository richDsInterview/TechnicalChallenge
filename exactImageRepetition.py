#!/usr/bin/env python

""" Richard Paul Armstrong 2018
Script to compare an image to all the images contained in a database
directory. If no identical copies, add it to the database

Arguments:
    infile : path to image file to compare
    dbDir : path to database directory containing comparison images
"""
import sys
import argparse
import os
import shutil
import cv2
import numpy as np

def compareImagesBinary(file1, file2):
    try:
        if open(file1, 'rb').read() == open(file2, 'rb').read():
            return True
    except IOError:
        print("One of the files is not an image file")
        return False

def compareImagesNumpy(file1, file2):
    return np.array_equal(cv2.imread(file1), cv2.imread(file2))

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")

    args = parser.parse_args(arguments)

    # if the test file is not an image file, fail
    if cv2.imread(args.infile) is None:
        exit()

    baseDir = os.path.abspath(args.dbDir)
    binaryMatch = False
    numpyMatch = False

    for dbImg in os.listdir(args.dbDir):
        absImgPath = baseDir + "/" + dbImg
        # if a file in the database directory is not an image file, ignore it
        if cv2.imread(absImgPath) is None:
            break

        # test if the input images are EXACTLY the same as any in the database directory
        if compareImagesBinary(args.infile, absImgPath):
            binaryMatch = True

        # test if the numpy representation of the image is the same as any in the database directory
        if compareImagesNumpy(args.infile, absImgPath):
            numpyMatch = True
            break

    # print the result
    if numpyMatch:
        print("Matching numpy representation to input image's found in database directory. Not adding")
    elif binaryMatch:
        print("Matching binary file found in database directory. Not adding")
    else:
        print("No match found. Adding ", args.infile, " to database directory: ", baseDir)
        shutil.copy(args.infile, baseDir)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))