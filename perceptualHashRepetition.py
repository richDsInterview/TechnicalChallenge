#!/usr/bin/env python

"""A simple python script to exactly compare an image to all the images contained in a database
    directory. The comparison should be sensitive to scaling and assumes, as per the question,
    that the scaling will be performed with common ratio.
Arguments:
    infile : path to image file to compare
    dbDir : path to database directory containing comparison images
Returns:
    Truth value echoed to command line
"""
import sys
import argparse
import os
import dhash
import PIL

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")

    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.dbDir)

    # test if an input image is broadly similar (blurring, scaling, noise-added) to any in the database directory

    score = 0.0
    # convert test image into numpy array
    try:
        imTest = PIL.Image.open(args.infile)
    except FileNotFoundError:
        # filename not an image file
        print("An error occured trying to read the file.")

    # loop through each image in the Test database
    for dbImg in os.listdir(args.dbDir):
        # convert current DB image into numpy array
        try:
            imDB = PIL.Image.open(baseDir + "/" + dbImg)
        except OSError:
            # filename not an image file
            continue
        if imTest is not None and imDB is not None:
            # hash, then compare the two images
            dh1 = dhash.dhash_int(imTest)
            dh2 = dhash.dhash_int(imDB)
            score = 1 - dhash.get_num_bits_different(dh1,dh2)/dh1.bit_length()

        else:
            print("comparison error with files %s and %s", imDB, imTest)

        if score >= 0.65:
            # print the result
            print("Matching image found in database directory: ", dbImg, " (score: ", str(score), ").")

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
