#!/usr/bin/env python
import os.path
import time

import win32com.client
from docx2pdf import convert
from fpdf import FPDF

from common import file_util
from fileconv.converter import FileConverter


class PDFConverter(FileConverter):
    def __init__(self):
        super(PDFConverter, self).__init__()
        self.images = []

    def trans_form(self, file_path):
        ext = file_util.get_file_ext(file_path)
        out_file_name = file_util.get_output_path(file_path, '.pdf')
        if os.path.exists(out_file_name):
            os.remove(out_file_name)
        if ext == "xlsx":
            from win32com.client import DispatchEx
            try:
                xlApp = DispatchEx("Excel.Application")
                xlApp.Visible = False
                xlApp.DisplayAlerts = 0
                books = xlApp.Workbooks.Open(file_path, False)
                books.ExportAsFixedFormat(0, out_file_name)
            except Exception as e:
                print(e)
            finally:
                books.Close(False)
                xlApp.Quit()
        elif ext == "docx":
            convert(file_path, out_file_name)
            return out_file_name
        elif ext in ['ppt', 'pptx']:
            ppt_app = win32com.client.Dispatch('PowerPoint.Application')
            ppt = ppt_app.Presentations.Open(file_path)
            ppt.SaveAs(out_file_name, 32)
            ppt_app.Quit()
            return out_file_name

    def images_to_pdf(self):
        pdf = FPDF()
        pdf.set_auto_page_break(0)  # 自动分页设为False
        out_file_name = str(time.process_time_ns()) + ".pdf"
        file_path = ""
        for image in sorted(self.images):
            file_path = file_util.get_file_path(image)
            pdf.add_page()
            pdf.image(image, w=190)  # 指定宽高
        out_file_name = os.path.join(file_path, out_file_name)
        pdf.output(out_file_name, "F")
        return out_file_name
