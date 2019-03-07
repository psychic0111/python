#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import importlib
import sys
from io import StringIO
import string
import os
from wand.image import Image

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

'''
解析PDF文件，获取各种内容
'''
def minerParser(pdf_path):

    fp = open(pdf_path, 'rb')   # 以二进制读模式打开

    # 文件对像创建PDF解析器
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()

        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 用来计数页面，图片，曲线，figure，水平文本框等对象的数量
        num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():
            num_page += 1
            interpreter.process_page(page)

            # 接受该页面的LTPage对象
            layout = device.get_result()
            for x in layout:
                if isinstance(x, LTImage):   # 图片
                    num_image += 1
                if isinstance(x, LTCurve):   # 曲线
                    num_curve += 1
                if isinstance(x, LTFigure): # figure对象
                    num_figure += 1
                if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
                    num_TextBoxHorizontal += 1

                    # 保存文本内容
                    with open(r'text.txt', 'a', encoding='gbk') as f:
                        result = x.get_text().strip()
                        f.write(result)
        print('对象数量：\n', '页面数：%s\n' % num_page, '图片数：%s\n' % num_image, '曲线数：%s\n' % num_curve, '水平文本框：%s\n'
              % num_TextBoxHorizontal)


def pdf2image(pdf_file):
    image_pdf = Image(filename=pdf_file, resolution=300)
    image_jpeg = image_pdf.convert('jpg')

    req_image = []
    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpg'))

    i = 0
    for img in req_image:
        folder = 'd:/testimage/'
        if not os.path.exists(folder):
            os.makedirs(folder)
        ff = open(folder + str(i) + '.jpg', 'wb')
        ff.write(img)
        ff.close()
        i += 1




if __name__ == '__main__':
    pdf_path = 'd:/阿里巴巴Java开发手册终极版v1.3.0.pdf'
    # minerParser(pdf_path)
    pdf2image(pdf_path)

