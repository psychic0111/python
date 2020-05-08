#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from skimage import data
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import pylab

image = data.binary_blobs()
plt.imshow(image, 'gray')
pylab.show()

image_color = data.astronaut()
plt.imshow(image_color)
pylab.show()

image_local = io.imread('e:/cf400dc4d7e128635f2e066f7497eb8b.jpg')
plt.imshow(image_local)
pylab.show()
