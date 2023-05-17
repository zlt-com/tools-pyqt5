
from common import file_util
from fileconv.converter import FileConverter


class ExcelConverter(FileConverter):
    def __init__(self):
        super(ExcelConverter, self).__init__()

    def transform(self, file_path, out_put_dir=""):
        ext = file_util.get_file_ext(file_path)

