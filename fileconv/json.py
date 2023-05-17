import pandas

from common import file_util
from fileconv.converter import FileConverter


class JsonConverter(FileConverter):
    def __init__(self):
        super(JsonConverter, self).__init__()

    def transform(self, file_path: str):
        ext = file_util.get_file_ext(file_path)
        if ext == "xlsx":
            out_file_name = file_util.get_output_path(file_path, ".json")
            excel = pandas.read_excel(file_path)
            excel.to_json(out_file_name)
            return out_file_name

