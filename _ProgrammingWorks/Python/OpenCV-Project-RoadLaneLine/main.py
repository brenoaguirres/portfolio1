#########################################################################
# PROJECT - ROAD LANE LINE DETECTOR
#########################################################################

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# >>>>>> STEPS <<<<<<<<<
# 1 - load image and convert to rgb
# 2 - define ROI (in this case, create a triangle and mask the other regions)
# 3 -

# NOTE: plt.show() displays yaxis from max value to min value, ex: 700 to 0


# STEP 1 <<<<<<<<<<<<<<<
image = cv.imread('road.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# print(image.shape)
height = image.shape[0]
width = image.shape[1]


# STEP 2 <<<<<<<<<<<<<<<
region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)  # create array of zeros with the shape of other image
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count  # the comma identifies a tuple, otherwise it will multiply 255 by c_count
    cv.fillPoly(mask, vertices, match_mask_color)  # will fill the mask with blank in all channels

    # return image only where pixel mask matches
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


cropped_image = region_of_interest(image, np.array([region_of_interest_vertices], np.int32))

plt.imshow(cropped_image)
plt.show()
