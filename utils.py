import math
import operator
from functools import reduce

import numpy as np
from PIL import ImageStat, ImageChops


def image_diff(img1, img2):
    """
    Calculates RGB difference between two images.
    :param img1:
    :param img2:
    :return: the distance between img1 and img2
    """
    difference = ImageStat.Stat(ImageChops.difference(img1, img2)).rms
    return sum(difference)


def rmsdiff(im1, im2):
    """
    Calculate the root-mean-square difference between two images
    :param im1:
    :param im2:
    :return: the rms difference of the two images.
    """
    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
                            map(lambda h, i: h * (i ** 2), h, range(256))
                            ) / (float(im1.size[0]) * im1.size[1]))


def sample_probability(p):
    return np.random.binomial(1, p) == 1
