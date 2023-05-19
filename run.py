import base64
import os

from PyQt5.QtCore import pyqtSignal, QThreadPool

from icon import Icon
from scan.scan import ParserResult
from common import file_util, constant
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QHeaderView

from threader.threader import ScanFileKeywordThread, ParserGovHtmlThread
from threader.threader import ParserGovHtmlSaveFileThread, FileConvertThread, ScanFileLogThread
from ui import Ui_MainPage


class Run(QtWidgets.QWidget, Ui_MainPage):
    def __init__(self):
        super(Run, self).__init__()
        self.setupUi(self)
        self.selected_dir = []  # 文件转换选择的文件
        self.save_dir = ''  # 文件转换保存到的文件夹
        self.files = []  # 文件转换的所有文件
        self.file_conv_progress_bar.hide()  # 默认文件转换进度条隐藏
        self.conv_count = 0  # 转换的个数
        self.init_file_type_select()  # 初始化转换文件界面的所有控件
        self.parser_html_file_names = []  # 解析html获取的文件名
        self.scan_files = []  # 扫描出来的文件
        self.parser_keyword_files = []  # 扫描出关键字的文件
        self.pool = QThreadPool()
        self.pool.globalInstance()
        self.pool.setMaxThreadCount(10)  # 设置最大线程数
        self.scan_threads = []  # 扫描线程组，全盘扫描

        # 初始化扫描磁盘下拉框
        disks = file_util.get_disklist()
        for d in disks:
            self.tab3_combox_select_disk.addItem(d, d)

        # 初始化扫描日志表格
        self.tab3_table_scan_files.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tab3_table_parser_files.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 文本框日志信号
        self.file_convert_log_text_signal.connect(self.write_file_convert_log)
        self.scan_file_log_text_signal.connect(self.write_scan_file_log)
        self.scan_file_keyword_signal.connect(self.write_parser_scan_file_log)
        self.parser_html_log_text_signal.connect(self.write_parser_html_log)

    def init_ui_text(self):
        self.selected_dir = []
        self.files = []
        self.conv_count = 0

    def init_file_type_select(self):
        for key in constant.source_file_type.keys():
            self.source_file_type_select.addItem(constant.source_file_type[key], key)

    def tab_change(self):
        if self.tab_main.currentIndex() == 2:
            self.tab3_combox_select_disk.clear()
            disks = file_util.get_disklist()
            for d in disks:
                self.tab3_combox_select_disk.addItem(d, d)

    '''
    以下为文件转换功能的所有函数
    '''

    def target_file_type_select_change(self):
        self.target_file_type_select.clear()
        target_key = constant.get_can_convert_file_type(self.source_file_type_select.currentData())
        for key in target_key:
            self.target_file_type_select.addItem(constant.file_type[key], key)

    # 文件选择按钮
    def btn_select_file(self):
        file_type = f"*.{self.source_file_type_select.currentData()}"
        if self.source_file_type_select.currentData() == "image":
            file_type = "*.jpg;*.jpeg;*.png"
        root = 'C:/Users/jerry/Documents/'
        self.selected_dir = QFileDialog.getOpenFileNames(self, caption='选择文件', directory=root, filter=file_type)
        self.file_conv_path.setText(';'.join(self.selected_dir[0]))

    # 选择转换后保存目录
    def file_conv_select_save_directory(self):
        self.save_dir = QFileDialog.getExistingDirectory(self, caption='选择转换保存文件夹', directory="")
        self.tab1_txt_file_save_directory.setText(self.save_dir)

    file_convert_log_text_signal = pyqtSignal(str)

    # 转换按钮
    def btn_conv(self):
        if self.file_conv_path.text() == "":
            QMessageBox.about(self, "提醒", "文件路径不能为空")
            return
        out_put_dir = self.tab1_txt_file_save_directory.text()
        # if not file_util.is_dir(out_put_dir):
        #     QMessageBox.about(self, "提醒", "文件转换后保存路径不能为空并真实存在")
        #     return
        self.init_ui_text()
        self.file_conv_result_text.setPlainText("开始转换：\r\n")
        self.file_conv_result_text.setPlainText("")
        self.file_conv_progress_bar.setValue(0)
        self.files = []
        file_path_text = self.file_conv_path.text()
        # 如果是文件夹就遍历
        if file_util.is_dir(file_path_text):
            file_type = self.source_file_type_select.currentData()
            self.files, _ = file_util.get_files_all(file_path_text, [file_type])
        # 不是文件夹就是文件
        else:
            self.files = file_path_text.split(";")
        # 有可转换文件
        log_file_name = ""
        if len(self.files) > 0:
            try:
                self.file_conv_progress_bar.setMaximum(len(self.files))
                self.file_conv_progress_bar.show()
                if self.source_file_type_select.currentData() == "image":
                    self.converter(self.files, out_put_dir)
                else:
                    for f in self.files:
                        log_file_name = f
                        self.converter(log_file_name, out_put_dir)
                while self.conv_count == len(self.files):
                    print("转换结束")
                    break
            except Exception as e:
                print(e)
                self.conv_count += 1
                self.file_conv_result_text. \
                        setPlainText(self.file_conv_result_text.toPlainText() + log_file_name + " 转换失败。" + "\r\n")
        # self.btn_file_conv.setDisabled(False)

    def converter(self, f, out_put_dir):
        from fileconv.factory import ConverterFactory
        try:
            converter = ConverterFactory(self.target_file_type_select.currentData()).get_converter()
            if self.source_file_type_select.currentData() == "image":
                converter.images = self.files
                converter.images_to_pdf(out_put_dir=out_put_dir)
                log_file_name = str(self.files)
                self.conv_count += len(self.files)
            else:
                converter.transform(f, out_put_dir=out_put_dir)
                log_file_name = f
                self.conv_count += 1
            self.file_conv_progress_bar.setValue(self.conv_count)
            self.file_conv_result_text.setText(f"{log_file_name} 转换为{self.target_file_type_select.currentText()}成功。\r\n{self.file_conv_result_text.toPlainText()}")
        except Exception as e:
            print(e)

    def converter_mutil_thread(self, f, out_put_dir):
        from fileconv.factory import ConverterFactory
        converter = ConverterFactory(self.target_file_type_select.currentData()).get_converter()
        if self.source_file_type_select.currentData() == "image":
            converter.images = self.files
            converter.images_to_pdf(out_put_dir=out_put_dir)
            self.conv_count += len(self.files)
        else:
            thread = FileConvertThread(converter, f, out_put_dir, self.file_convert_log_text_signal)
            self.pool.start(thread)

    def write_file_convert_log(self, text):
        self.conv_count += 1
        self.file_conv_progress_bar.setValue(self.conv_count)
        self.file_conv_result_text.setPlainText(text + "\r\n" + self.file_conv_result_text.toPlainText())

    '''
    以下为网站文件网页解析
    '''
    parser_html_log_text_signal = pyqtSignal(str)

    def parser_web_site_content(self):
        try:
            thread = ParserGovHtmlThread(self.tab2_txt_web_url.text(),
                                         self.parser_html_log_text_signal,
                                         self.tab2_txt_key.text())
            self.pool.start(thread)
            for i in range(2, 22):
                url = self.tab2_txt_web_pages.text().format(str(i))
                thread = ParserGovHtmlThread(url, self.parser_html_log_text_signal, self.tab2_txt_key.text())
                self.pool.start(thread)
            thread = ParserGovHtmlSaveFileThread(self)
            self.pool.start(thread)
        except Exception as e:
            print(e)

    def write_parser_html_log(self, text):
        text = text.replace("扎鲁特旗人民政府办公室关于", "") \
            .replace("扎鲁特旗人民政府关于", "") \
            .replace("中共扎鲁特旗委办公室", "") \
            .replace("印发", "") \
            .replace("《", "") \
            .replace("》", "") \
            .replace(" ", "") \
            .replace("的通知", "")
        self.parser_html_file_names.extend(text.split("\r\n"))
        self.tab2_text_content.setText(text + "\r\n" + self.tab2_text_content.toPlainText())

    '''
    以下为保密关键字扫描
    '''
    scan_file_log_text_signal = pyqtSignal(str)
    scan_file_keyword_signal = pyqtSignal(ParserResult)

    # 开始扫描并处理
    def scan_disk(self):
        if self.tab3_btn_scan.text() == "停止扫描":
            for thread in self.scan_threads:
                thread.pause()
            self.tab3_btn_scan.setText("继续扫描")
            return
        elif self.tab3_btn_scan.text() == "继续扫描":
            for thread in self.scan_threads:
                thread.resume()
            self.tab3_btn_scan.setText("停止扫描")
            return
        self.scan_threads = []
        if self.tab3_checkbox_scan_all_disk.isChecked():
            disks = file_util.get_disklist()
            for disk in disks:
                scan_thread = ScanFileLogThread(disk=disk, signal=self.scan_file_log_text_signal)
                self.scan_threads.append(scan_thread)
        else:
            d = self.tab3_combox_select_disk.currentText()
            scan_thread = ScanFileLogThread(disk=d, signal=self.scan_file_log_text_signal)
            self.scan_threads.append(scan_thread)
        for st in self.scan_threads:
            self.pool.start(st)
        self.tab3_btn_scan.setText("停止扫描")

    # 扫描日志写入文本框
    def write_scan_file_log(self, text):
        if text == "done" or self.pool.activeThreadCount() == 0:
            self.tab3_btn_scan.setText("开始扫描")

        self.scan_files.append(text)
        row_count = self.tab3_table_scan_files.rowCount()
        self.tab3_table_scan_files.insertRow(row_count)
        self.tab3_table_scan_files.setItem(row_count, 0, QtWidgets.QTableWidgetItem(text))
        self.tab3_table_scan_files.scrollToBottom()
        tab_title = "扫描可分析文件({0})".format(len(self.scan_files))
        self.tab_scan_result.setTabText(0, tab_title)
        parser_thread = ScanFileKeywordThread(ui.scan_file_keyword_signal, text,
                                              keyword=ui.tab3_text_keywords.toPlainText().split(" "))
        self.pool.start(parser_thread)

    def write_parser_scan_file_log(self, result):
        if len(result.keys) > 0:
            self.parser_keyword_files.append(result.file)
        for i in range(len(result.keys)):
            row_count = self.tab3_table_parser_files.rowCount()
            self.tab3_table_parser_files.insertRow(row_count)
            self.tab3_table_parser_files.setItem(row_count, 0, QtWidgets.QTableWidgetItem(result.file))
            self.tab3_table_parser_files.setItem(row_count, 1, QtWidgets.QTableWidgetItem(result.keys[i]))
            self.tab3_table_parser_files.setItem(row_count, 2, QtWidgets.QTableWidgetItem(result.context[i]))
            self.tab3_table_parser_files.scrollToBottom()
        tab_title = "包含关键字文件数量({0})".format(len(self.parser_keyword_files))
        self.tab_scan_result.setTabText(1, tab_title)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Run()
    with open('tmp.ico', 'wb') as tmp:
        tmp.write(base64.b64decode(Icon().img))
    # ico_path = os.path.join(os.path.dirname(__file__), './resource/logo.ico')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QBitmap("tmp.ico"))
    ui.setWindowIcon(icon)
    ui.show()
    os.remove("tmp.ico")
    sys.exit(app.exec_())
