###################################################################################
# CLASS 1 - TILT SHIFT EFFECTS IN OPENCV
###################################################################################

# Tilt Shift - Effect that takes a normal image, usually a landscape or top down, and make it looks like it's a
#   miniaturized model.
#   It does that by focusing certain areas, and blurring others, sort like a fake "bokeh" - photography term for
#   lens blur. Means blur in japanese. - when you have a low aperture, like for example, 1.8, the focal point remains
#   the same but the background gets blurry.

import cv2 as cv
import math
import os
import numpy as np
import scipy.signal
import shutil


def generating_kernel(parameter):
    # returns a 5x5 generating kernel based on an input parameter.
    # Args:
    # parameter (float): range of value: [0, 1].

    kernel = np.array([0.25 - parameter / 2.0, 0.25, parameter,
                       0.25, 0.25 - parameter / 2.0])
    return np.outer(kernel, kernel)  # outer product (k*k) of two vectors


def reduce_img(image):
    # Convolve the input image with a generating kernel of 0.4 and then reduce its width and height by two
    # Return rows from 0 to output.shape[0] (n of rows) with step 2, and cols from 0 to output.shape[1] (n of cols)
    #   with step 2.
    # Args:
    # image (numpy.ndarray): a grayscale image of shape (r, c).
    kernel = generating_kernel(0.4)

    output = scipy.signal.convolve2d(image, kernel, 'same')

    return output[:output.shape[0]:2, :output.shape[1]:2]


def expand(image):
    pass


def gauss_pyramid(image, levels):
    pass


def lapl_pyramid(gauss_pyr):
    pass


def blend(lapl_pyr_white, lapl_pyr_black, gauss_pyr_mask):
    pass


def collapse(pyramid):
    pass


def run_blend(black_image, white_image, mask):
    pass


def get_images(sourceFolder):
    pass


# Main Program
def main():
    pass


main()
