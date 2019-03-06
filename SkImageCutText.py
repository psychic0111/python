#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pylab

import skimage.data as data
import skimage.segmentation as seg
import skimage.filters as filters
import skimage.draw as draw
import skimage.color as color
import skimage.io as io

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax


text = io.imread('C:/Users/ZF95/Desktop/测试图片/text1.jpg', as_grey=True)
#text = data.text()
# fig, ax = plt.subplots(1, 1)
# ax.hist(text.ravel(), bins=32, range=[0, 256])
# ax.set_xlim(0, 256)
image_show(text)
pylab.show()

# text_segmented = text > 0
# image_show(text_segmented)
# pylab.show()
#
# text_segmented = text > 10
# image_show(text_segmented)
# pylab.show()
#
# text_segmented = text > 20
# image_show(text_segmented)
# pylab.show()

# text_local = filters.threshold_local(text, block_size=51, offset=10)
# image_show(text > text_local)
# pylab.show()

text_otsu = filters.threshold_otsu(text)
image_show(text <= text_otsu)
pylab.show()

text_li = filters.threshold_li(text)
image_show(text <= text_li)
pylab.show()

text_yen = filters.threshold_yen(text)
image_show(text > text_yen)
pylab.show()

text_iso = filters.threshold_isodata(text)
image_show(text > text_iso)
pylab.show()
