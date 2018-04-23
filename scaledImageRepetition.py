#!/usr/bin/env python

""" Richard Paul Armstrong 2018
A simple python script to exactly compare an image to all the images contained in a database
directory. The comparison should be sensitive to scaling and assumes, as per the question,
that the scaling will be performed with common ratio.

Arguments:
    infile : path to image file to compare
    dbDir : path to database directory containing comparison images
"""
import sys
import argparse
import os
import numpy as np
import cv2
import shutil

# compareScaled: a method to compare two images that are possibly scaled versions of each
# other. Optional arguments are to first convert to thumbnail representations, to quantise
# colour information (make greyscale), and quantise pixel values.
def compareScaled(im1, im2, thumb=True, grey=False, pixelQuant=8, gridsize=16):
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

    #scale by the pixel quantisation amount
        im1 = im1//pixelQuant
        im2 = im2//pixelQuant

    # return the Hamming difference between the two images and the difference image
    score = 1 - np.count_nonzero(im1 != im2)/im1.size
    diff = np.abs(im1-im2)
    return score, diff

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="path to file to compare") #, type=argparse.FileType('r'))
    parser.add_argument('dbDir', help="path to 'Database' directory")
    parser.add_argument('-t', help="make thumbnail image", action="store_true")
    parser.add_argument('-g', help="make greyscale/flatten colour information", action="store_true")
    parser.add_argument('-q', help="pixel quantisation factor 2^x (default 2^8)", type=int, default=8)
    parser.add_argument('--threshold', help="threshold val (default 0.5)", type=float, default=0.5)


    args = parser.parse_args(arguments)
    baseDir = os.path.abspath(args.dbDir)

    match = False
    score = 0.0

    try:
        imTest = cv2.imread(args.infile)
        shape = imTest.shape
    except IOError:
        # filename not an image file
        print("An error occurred trying to read the file.")
        exit()
    except AttributeError:
        print("An error occurred trying to read the input file. Is it an image file?")
        exit()

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
        score, diff = compareScaled(imDB, imTest, thumb=args.t, grey=args.g, pixelQuant=args.q)

        if score >= args.threshold:
            match = True
            # print the result
            print("Matching image found in database directory: ", dbImg, " (score: ", str(score), ")")


    if match:
        print("Match(es) found. Not adding")
    else:
        print("No match found. Adding ", args.infile, " to database directory: ", baseDir)
        shutil.copy(args.infile, baseDir)



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


def get_num_bits_different(hash1, hash2):
    return bin(hash1 ^ hash2).count('1')