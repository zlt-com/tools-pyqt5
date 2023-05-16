import os
import time

import cv2
import fitz

from common import file_util
from fileconv.converter import FileConverter


class ImageConverter(FileConverter):
    def __init__(self):
        super(ImageConverter, self).__init__()
        self.file_name = ""
        self.files = []
        self.images = []

    def trans_form(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "pdf":
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
                cv2.imwrite(os.path.join(file_util.get_file_path(file_path), str(time.process_time_ns()) + ".png"),
                            result)

    def image_h_concat(self):
        images = []
        for f in self.files:
            img = cv2.imread(f)
            images.append(img)
        cv2.imwrite(self.file_name, cv2.hconcat(images))

    def image_v_concat(self):
        images = []
        for f in self.files:
            img = cv2.imread(f)
            images.append(img)
        cv2.imwrite(self.file_name, cv2.vconcat(images))


