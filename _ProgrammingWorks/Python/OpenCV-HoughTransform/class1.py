################################################################
# HOUGH LINES TRANSFORM THEORY
################################################################

# Hough Transform - Popular technique to detect any shape if you can represent the shape in a mathematical form.
#   - Can detect even if the shape is broken or distorted a little.

# a line can be expressed in image by:
# cartesian coordinates system: y = m*x + c
#       c = y intercept ;; m = slope of the line
# polar coordinates system: x*cosθ + y*sinθ = r

# mc space (hough space)
# c -> is the y axis ;; m -> is the x axis ;;
# the line is represented as a single point
# a point in the xy space can be represented as a line in the mc space
#   xy point -> xy ;; hough space line -> c = -xm + y // slope -> -x // intercept -> y

# the hough transform is about converting points in the xy space to lines in the mc/hough space
# the intersection point of all the lines will be the mc coordinate

# In the polar coordinate system
# r = x*cosθ + y*sinθ  and  y = (-cosθ/sinθ)*x + (r/sinθ)
#   θ is the angle of the line // r is the distance from the origin to the line
# in this case the hough space is the rθ space
# this representation will look like a sine curve using this equation r = x*cosθ + y*sinθ

# Briefly, a line in the image space can be expressed by two variables:
# cartesian -> y = mx + c
# polar -> xcosθ + ysinθ
# the cartesian can't represent vertical lines, so generally we use the polar

# Hough transform algorithm:
# 1) Edge detection, using canny edge detector
# 2) Mapping of edge points to the Hough space and storage using an accumulator
# 3) Interpretation of the accumulator to yield lines of infinite length. The interpretation is done by thresholding
#       and other possible constraints.
# 4) Conversion of infinite lines to finite lines

# OpenCV implements two kinds of Hough Line Transform
# 1) The standard -> (HoughLines method)
# 2) The probabilistic -> (HoughLinesP method)
