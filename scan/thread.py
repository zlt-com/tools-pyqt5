import os

from PyQt5.QtCore import QThread, QRunnable

from common import file_util
from scan.scan import ScanFile


# 扫描文件关键字进程
class ScanFileLogThread(QThread):
    file_types = ["docx", "txt", "pdf", "xlsx", "html"]

    def __int__(self):
        super(ScanFileLogThread, self).__init__()
        self.disk = ""
        self.ui = None

    def iter_file(self, disk):
        try:
            fs = os.listdir(disk)
            for f in fs:
                if f[0] in [".", "$"]:
                    continue
                f = os.path.join(disk, f)
                if os.path.isdir(f):
                    self.iter_file(f)
                else:
                    ext = file_util.get_file_ext(f)
                    if ext in self.file_types:
                        self.ui.scan_file_log_text.emit(f)
        except Exception as e:
            print(e)

    def run(self):
        self.iter_file(self.disk)


# 解析到关键字的文件
class ScanFileKeywordThread(QRunnable):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.file = ""

    def run(self):
        scan = ScanFile(self.file)
        file_path = scan.parser_file()
        if file_path != "":
            self.ui.scan_file_keyword_signal.emit(file_path)

