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
import numpy as np
import cv2

def compareScaled(im1, im2, thumb=True, grey=False, pixelQuant=True, gridsize=16, pixMax=2^4):
    # if desired, convert both images to thumbnails of specified size
    if thumb:
        im1 = cv2.resize(im1, dsize=(gridsize, gridsize))
        im2 = cv2.resize(im2, dsize=(gridsize, gridsize))
    # otherwise, convert images to a common grid, the smellest of the two
    # assumes reasonable scale relationship between images
    else:
        if im1.size<im2.size:
            im2 = cv2.resize(im2, dsize=(im1.shape[1], im1.shape[0]))
        else:
            im1 = cv2.resize(im1, dsize=(im2.shape[1], im2.shape[0]))
    # if desired, convert images to greyscale using the OpenCV library
    if grey:
        im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    if pixelQuant:
        im1 = im1//pixMax
        im2 = im2//pixMax

    # return the
    score = 1 - np.count_nonzero(im1 != im2)/im1.size
    diff = np.abs(im1-im2)
    return score, diff

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")

    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.dbDir)

    # test if the potentially scaled input image is the same as any in the database directory
    match = False
    score = 0.0
    # convert test image into numpy array
    try:
        imTest = cv2.imread(args.infile)
        shape = imTest.shape
    except IOError:
        # filename not an image file
        print("An error occured trying to read the file.")
    except AttributeError:
        print("An error occured trying to read the input file. Is it an image file?")
        exit()

    #, and then scale to thumbnail size
    #thumbTest = thumb(imTest)
    # loop through each image in the Test database
    for dbImg in os.listdir(args.dbDir):
        # convert current DB image into numpy array
        try:
            imDB = cv2.imread(baseDir + "/" + dbImg)
            shape = imDB.shape
        except IOError:
            # filename not an image file: ignore
            continue
        except AttributeError:
            # a file in the input database directory is not converting to a numpy array correctly. \
            # Ignore this file and move to the next
            continue

        # compare the two images
        score, diff = compareScaled(imDB, imTest)

        if score >= 0.45:
            match = True
            # print the result
            print("Exact matching image found in database directory: ", dbImg, " (score: ", str(score), ").")




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


def get_num_bits_different(hash1, hash2):
    return bin(hash1 ^ hash2).count('1')