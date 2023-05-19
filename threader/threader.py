import os
import shutil

from PyQt5.QtCore import QRunnable, QWaitCondition, QMutex

from common import file_util
from scan.scan import ScanFile


# 扫描文件关键字进程
class ScanFileLogThread(QRunnable):
    file_types = ["docx", "txt", "pdf", "xlsx", "html"]

    def __init__(self, signal, disk):
        super().__init__()
        self.disk = disk
        self.signal = signal
        self._isPause = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeAll()

    def iter_file(self, disk):
        try:
            fs = os.listdir(disk)
            for f in fs:
                self.mutex.lock()
                if self._isPause:
                    self.cond.wait(self.mutex)
                if f[0] in [".", "$"]:
                    self.mutex.unlock()
                    continue
                f = os.path.join(disk, f)
                if os.path.isdir(f):
                    self.mutex.unlock()
                    self.iter_file(f)
                else:
                    ext = file_util.get_file_ext(f)
                    if ext in self.file_types:
                        self.signal.emit(f)
                    self.mutex.unlock()
        except Exception as e:
            print(e)

    def run(self):
        self.iter_file(self.disk)
        self.signal.emit("done")


# 解析到关键字的文件
class ScanFileKeywordThread(QRunnable):
    def __init__(self, signal, file, keyword):
        super().__init__()
        self.signal = signal
        self.file = file
        self.keyword = keyword

    def run(self):
        try:
            scan = ScanFile(self.file, self.keyword)
            result = scan.parser_file()
            if result.file != "":
                self.signal.emit(result)
        except Exception as e:
            print(e)


class ParserGovHtmlThread(QRunnable):
    def __init__(self, url, signal, tag):
        super().__init__()
        self.url = url
        self.signal = signal
        self.tag = tag

    def run(self):
        try:
            from web import parser_gov
            content = parser_gov.parser(self.url, self.tag)
            self.signal.emit(content)
        except Exception as e:
            print(e)


class ParserGovHtmlSaveFileThread(QRunnable):

    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def run(self):
        try:
            while True:
                if self.ui.pool.activeThreadCount() == 1:
                    scan_path = "D:/政府办/政府文件"
                    files, dirs = file_util.get_files_all(scan_path)
                    html_files = self.ui.parser_html_file_names
                    for file in files:
                        for hf in html_files:
                            if file.find(hf) > 0:
                                print(file)
                                out_put_name = os.path.basename(file)
                                out_put_path = scan_path + '/publish/'
                                shutil.copyfile(file, out_put_path + out_put_name)
                    break
        except Exception as e:
            print(e)


class FileConvertThread(QRunnable):
    def __init__(self, converter, f, out_put_dir, signal):
        super().__init__()
        self.signal = signal
        self.converter = converter
        self.f = f
        self.out_put_dir = out_put_dir

    def run(self):
        try:
            # print("执行转换：" + self.f)
            self.converter.transform(self.f, out_put_dir=self.out_put_dir)
            self.signal.emit(self.f)
        except Exception as e:
            print(self.f, e)
