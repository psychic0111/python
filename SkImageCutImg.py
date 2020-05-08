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
    ax.imshow(image, cmap=cmap)
    ax.axis('off')
    plt.show()
    return fig, ax


image = io.imread('e:/cf400dc4d7e128635f2e066f7497eb8b.jpg')
plt.imshow(image)
plt.show()
#
image_gray = color.rgb2gray(image)
image_show(image_gray)

def circle_points(resolution, center, radius):
    radians = np.linspace(0, 2*np.pi, resolution)
    c = center[1] + radius * np.cos(radians)
    r = center[0] + radius * np.sin(radians)

    return np.array([c, r]).T


print(type(image))  #显示类型
print(image.shape)  #显示尺寸
print(image.shape[0])  #图片高度
print(image.shape[1])  #图片宽度
print(image.shape[2])  #图片通道数
print(image.size)   #显示总像素个数
print(image.max())  #最大像素值
print(image.min())  #最小像素值
print(image.mean()) #像素平均值
print(image[0][0])#图像的像素值

points = circle_points(550, [180, 170], 100)[:-1]


snake = seg.active_contour(image, points)
snake = seg.active_contour(image_gray, points, alpha=0.06, beta=0.3)
fig, ax = image_show(image)
ax.plot(points[:, 0], points[:, 1], '--r', lw=3)

ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
plt.show()

image_labels = np.zeros(image_gray.shape, dtype=np.uint8)

indices = draw.circle_perimeter(100, 279, 20)
image_labels[indices] = 1
image_labels[points[:, 1].astype(np.int), points[:, 0].astype(np.int)] = 2
image_show(image_labels)
plt.show()

image_segmented = seg.random_walker(image_gray, image_labels, beta=39000)
fig, ax = image_show(image_gray)
plt.show()

ax.imshow(image_segmented == 1, alpha=0.3)
plt.show()
