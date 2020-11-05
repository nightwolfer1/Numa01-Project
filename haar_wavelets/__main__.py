#!/usr/bin/env python3

"""
Detta är huvudfilen, utifrån vilken resterande saker
körs

Ansvarig: Emil Eriksson
"""

import argparse
from skimage import io, color
import numpy as np
import haar_wavelets.haarcompression as com
import haar_wavelets.inversehaar as inv
import haar_wavelets.transformarray as ta

# Parsing of arguments begins
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--compress", type=int,
                    help="Compresses a bitmap using Haar Transformation, iterating this number of times")
parser.add_argument("-r", "--reverse", type=int,
                    help="Does inverse Haar transformation this many times")
parser.add_argument("-i", "--input", type=str,
                    help="Path to file operated on")
parser.add_argument("-o", "--output", type=str, default="./haar_output.jpg",
                    help="Path to output, defaults to current directory")
args = parser.parse_args()


# Functions to be used
def compress(image_array):
    # Checks if array is even (trash is not used)
    num_rows, num_cols = np.shape(image_array)
    # Checks rows
    if (num_rows % 2) != 0:
        image_array = np.delete(image_array, -1, 0) # Removes last row
    # Checks coloumns
    if (num_cols % 2) != 0:
        image_array = np.delete(image_array, -1, 1) # Removes last coloumn

    # args.compress is number of iterations
    return com.haar_compression(image_array, args.compress)

def reverse_transform(image_array):
    num_rows, num_cols = np.shape(image_array)
    # Raises error if this doesn't looks like it was transformed in the first place
    # Checks rows and coloumns
    if (num_rows % 2) != 0 or (num_cols % 2) != 0:
        raise ValueError("This image does not have even dimensions, and does not seem to have been transformed in the first place")

    wm = ta.create_haar_array(num_rows) # Rows
    wn = ta.create_haar_array(num_cols) # Coloumns
    return inv.inverse_haar_transformation(image_array, wm, wn, args.reverse)


def main():
    # If the user has no idea what they're doing (most of them)
    if not args.input:
        exit("Input path must be defined, use \'hwnuma --help\' for more info")
    if not args.compress and not args.reverse:
        exit("No operation defined, use \'hwnuma --help\' for more info")
    
    # Creates Haar array of picture
    image_array = io.imread(args.input)
    # Remove RBG info from image_array
    if len(np.shape(image_array)) > 2:
        image_array = color.rgb2gray(image_array)

    if args.compress:
        output_data = compress(image_array)
    elif args.reverse:
        output_data = reverse_transform(image_array)

    # Writes to output
    output_path = args.output
    # We want output to end in jpg
    if not output_path.endswith(".jpg"):
        output_path += ".jpg"
        
    io.imsave(output_path, output_data)

if __name__ == "__main__":
    main()