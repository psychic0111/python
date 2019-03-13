#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import importlib
import sys
import os
from wand.image import Image

importlib.reload(sys)

import fitz
import time
import re

def muPdfParser(pdf_path, pic_path):
    t0 = time.clock()

    # 使用正则表达式来查找图片
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"

    doc = fitz.open(pdf_path)

    imgcount = 0
    lenXREF = doc._getXrefLength()

    # 打印PDF的信息
    print("文件名:{}, 页数: {}, 对象: {}".format(pdf_path, len(doc), lenXREF - 1))

    for i in range(3, lenXREF):
        text = doc._getXrefString(i)
        isObject = re.search(checkXO, text)
        isImage = re.search(checkIM, text)

        if not isObject or not isImage:
            continue

        imgcount += 1

        pix = fitz.Pixmap(doc, i)

        new_name = "_img{}.png".format(imgcount)

        new_name = new_name.replace(':', '')

        #pix0 = fitz.Pixmap(fitz.csGRAY, pix)
        #pix0.writePNG(os.path.join(pic_path, new_name))
        #pix0 = None

        pix.writePNG(os.path.join(pic_path, new_name))
        pix = None

        t1 = time.clock()
        print("运行时间:{}s".format(t1 - t0))
        print("提取了{}张图片".format(imgcount))


if __name__ == '__main__':

    pdf_path = 'd:/周易大传今注·高亨.pdf'
    pic_path = 'D:/testimage'

    muPdfParser(pdf_path, pic_path)

