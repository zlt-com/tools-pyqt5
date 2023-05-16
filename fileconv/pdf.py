#!/usr/bin/env python
import os.path
import tempfile
import time

import cv2
from io import BytesIO

import fitz
from pdf2docx import Converter
from pdf2image import convert_from_path
from pdfminer.converter import TextConverter, HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from common import file_util


def pdf_to_docx(file_path):
    conv = Converter(file_path)
    out_file_name = file_util.get_output_path(file_path, ".docx")
    conv.convert(out_file_name)
    conv.close()
    return out_file_name


def pdf_to_txt(file_path):
    # with pdfplumber.open(file_path) as pdf:
    #     for page in pdf.pages:
    #         txt_file = codecs.open(common.get_output_path(file_path, ".txt"), 'a', 'utf-8')
    #         txt_file.write(page.extract_text())
    #         txt_file.close()
    out_file_name = file_util.get_output_path(file_path, ".txt")
    output = open(out_file_name, 'w', encoding='utf-8')
    rm = PDFResourceManager()
    lap = LAParams()
    device = TextConverter(rm, output, laparams=lap)
    with open(file_path, 'rb') as fp:
        interpreter = PDFPageInterpreter(rm, device)
        for page in PDFPage.get_pages(fp, check_extractable=True):
            interpreter.process_page(page)
    device.close()
    output.close()
    return out_file_name


def pdf_to_html(file_path):
    out_file_name = file_util.get_output_path(file_path, ".html")
    output = open(out_file_name, 'w', encoding='utf-8')
    source_io = BytesIO()
    rm = PDFResourceManager()
    lap = LAParams()
    device = HTMLConverter(rm, source_io, laparams=lap, codec='utf-8')
    with open(file_path, 'rb') as fp:
        interpreter = PDFPageInterpreter(rm, device)
        for page in PDFPage.get_pages(fp, check_extractable=True):
            interpreter.process_page(page)
    output.write(source_io.getvalue().decode('utf-8'))
    device.close()
    output.close()
    return out_file_name


def pdf_to_image(file_path):
    pdf_doc = fitz.open(file_path)
    image_dir_name = "concat_images"
    image_path = os.path.join(file_util.get_file_path(file_path), image_dir_name)
    image_names = []
    for pg in range(0, pdf_doc.page_count):
        page = pdf_doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 1.33333333
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(image_path):  # 判断存放图片的文件夹是否存在
            os.makedirs(image_path)  # 若图片文件夹不存在就创建
        image_name = image_path + '\\' + 'images_%s.png' % pg
        pix.save(image_name)  # 将图片写入指定的文件夹内
        image_names.append(image_name)
    if len(image_names) > 1:
        images = []
        for img in image_names:
            image = cv2.imread(img)
            images.append(image)
            os.remove(img)
        result = cv2.vconcat(images)
        cv2.imwrite(os.path.join(file_util.get_file_path(file_path), str(time.process_time_ns()) + ".png"), result)


# 需要poppler
def pdf_to_image2(file_path):
    image_path = os.path.join(file_util.get_file_path(file_path), file_util.get_file_shot_name(file_path))
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(file_path, output_folder=path, last_page=1, first_page=0)
        base_filename = os.path.splitext(os.path.basename(file_path))[0] + '.jpg'
        for page in images_from_path:
            page.save(os.path.join(image_path, base_filename), 'JPEG')
