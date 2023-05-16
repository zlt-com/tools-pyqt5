#!/usr/bin/env python
import os.path

import comtypes
from docx2pdf import convert


from common import file_util
from fileconv.converter import FileConverter


class PDFConverter(FileConverter):
    def __init__(self):
        super(PDFConverter, self).__init__()

    def trans_form(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "xlsx":
            from win32com.client import DispatchEx
            out_file_name = file_util.get_output_path(file_path, ".pdf")
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
            out_file_name = file_util.get_output_path(file_path, '.pdf')
            if os.path.exists(out_file_name):
                os.remove(out_file_name)
            convert(file_path, out_file_name)
            return out_file_name
        elif ext in ['ppt', 'pptx']:
            out_file_name = file_util.get_output_path(file_path, '.pdf')
            if os.path.exists(out_file_name):
                os.remove(out_file_name)
            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            powerpoint.Visible = 1
            deck = powerpoint.Presentations.Open(file_path)
            deck.SaveAs(out_file_name, 32)  # formatType = 32 for ppt to pdf
            deck.Close()
            return out_file_name

