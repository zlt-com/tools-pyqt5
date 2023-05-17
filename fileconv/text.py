import docx2txt
import pandas
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from common import file_util
from fileconv.converter import FileConverter


class TxtConverter(FileConverter):
    def __init__(self):
        super(TxtConverter, self).__init__()

    def transform(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "docx":
            out_file_name = file_util.get_output_path(file_path, '.txt')
            text = docx2txt.process(file_path)
            out_file = open(out_file_name, "w", encoding='utf-8')
            out_file.write(text)
            out_file.close()
            return out_file_name
        elif ext == "pdf":
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
        elif ext == "xlsx":
            out_file_name = file_util.get_output_path(file_path, ".txt")
            excel = pandas.read_excel(file_path)
            excel.to_string(out_file_name)
