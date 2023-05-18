from pdf2docx import Converter

from common import file_util
from fileconv.converter import FileConverter
from win32com.client import Dispatch




class DocxConverter(FileConverter):
    def __init__(self):
        super(DocxConverter, self).__init__()

    def transform(self, file_path, out_put_dir=""):
        ext = file_util.get_file_ext(file_path)
        out_file_name = file_util.get_output_path(file_path, ".docx", out_put_dir)
        if ext == "pdf":
            conv = Converter(file_path)
            conv.convert(out_file_name)
            conv.close()
            return out_file_name
        elif ext == "doc":
            word = Dispatch("Word.Application")
            doc = word.Documents.Open(file_path)
            doc.SaveAs(out_file_name)
