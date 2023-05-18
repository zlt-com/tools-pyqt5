from common import file_util


class ScanFile:
    def __init__(self, file):
        self.file = file

    def parser_file(self):
        ext = file_util.get_file_ext(self.file)
        if ext == "html":
            return self.file
        else:
            return ""
