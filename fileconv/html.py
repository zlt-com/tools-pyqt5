from io import BytesIO

import mammoth
import pandas
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from common import file_util
from fileconv.converter import FileConverter


class HtmlConverter(FileConverter):
    def __init__(self):
        super(HtmlConverter, self).__init__()

    def transform(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "docx":
            out_file_name = file_util.get_output_path(file_path, '.html')
            with open(file_path, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                html = result.value
                out_file = open(out_file_name, "w", encoding='utf-8')
                out_file.write(html)
                out_file.close()
            return out_file_name
        elif ext == "pdf":
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
        elif ext == "xlsx":
            out_file_name = file_util.get_output_path(file_path, ".html")
            excel = pandas.read_excel(file_path)
            excel.to_html(out_file_name)
            return out_file_name
