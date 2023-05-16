import pandas

from common import file_util
from fileconv.converter import FileConverter


class CsvConverter(FileConverter):
    def __init__(self):
        super(CsvConverter, self).__init__()

    def trans_form(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "xlsx":
            out_file_name = file_util.get_output_path(file_path, ".csv")
            excel = pandas.read_excel(file_path)
            excel.to_csv(out_file_name, header=True)
            return out_file_name

