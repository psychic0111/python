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

image_local = io.imread('C:/Users/ZF95/Desktop/测试图片/1.jpg')
plt.imshow(image_local)
pylab.show()
