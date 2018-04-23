#!/usr/bin/env python

""" Richard Armstrong 2018
Script to compare an image to all the images contained in a database
    directory. if an input image is broadly similar (blurring, scaling,
    noise-added) to any in the database directory, discard it.
Arguments:
    infile : path to image file to compare
    dbDir : path to database directory containing comparison images
"""
import sys
import argparse
import os
import shutil
import dhash
import PIL

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")
    parser.add_argument('--threshold', help="threshold val (default 0.75)", type=float, default=0.75)

    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.dbDir)

    # test

    score = 0.0
    match = False
    # convert test image into numpy array
    try:
        imTest = PIL.Image.open(args.infile)
    except FileNotFoundError:
        # filename not an image file
        print("An error occured trying to read the test file. Can't compare")
        exit()

    # loop through each image in the Test database
    for dbImg in os.listdir(args.dbDir):
        # convert current DB image into numpy array
        try:
            imDB = PIL.Image.open(baseDir + "/" + dbImg)
        except OSError:
            # filename not an image file accessible by PIL. Ignore, quit this loop, and continue.
            continue

        if imTest is not None and imDB is not None:
            # hash, then compare the two images
            dh1 = dhash.dhash_int(imTest)
            dh2 = dhash.dhash_int(imDB)
            score = 1 - dhash.get_num_bits_different(dh1,dh2)/dh1.bit_length()
        else:
            print("comparison error with files %s and %s", imDB, imTest)

        if score > args.threshold:
            # alert about the match
            print("Matching image found in database directory: ", dbImg, " (score: ", str(score), ").")
            match = True

    if match:
        print("Match(es) found. Not adding")
    else:
        print("No match found. Adding ", args.infile, " to database directory: ", baseDir)
        shutil.copy(args.infile, baseDir)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
