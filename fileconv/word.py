from pdf2docx import Converter

from common import file_util
from fileconv.converter import FileConverter


class DocxConverter(FileConverter):
    def __init__(self):
        super(DocxConverter, self).__init__()

    def trans_form(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "pdf":
            conv = Converter(file_path)
            out_file_name = file_util.get_output_path(file_path, ".docx")
            conv.convert(out_file_name)
            conv.close()
            return out_file_name
