from common import file_util
import pandas


from common import file_util
from fileconv.converter import FileConverter


class ExcelConverter(FileConverter):
    def __init__(self):
        super(ExcelConverter, self).__init__()

    def trans_form(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
