import os
import time

from common import file_util
from fileconv import pdf
from fileconv import word
import threading
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ui import Ui_MainPage


class Run(QtWidgets.QWidget, Ui_MainPage):
    def __init__(self):
        super(Run, self).__init__()
        self.setupUi(self)
        self.selected_dir = []
        self.files = []
        self.file_conv_progress_bar.hide()
        self.conv_count = 0
        self.done = " 转换成功"

    def init_ui_text(self):
        self.selected_dir = []
        self.files = []
        self.conv_count = 0
        self.done = " 转换成功"

    # 文件选择按钮
    def btn_select_file(self):
        # self.selected_dir = QFileDialog.getExistingDirectory(self, caption='选择文件夹', directory=os.getcwd())
        file_type = "*.pdf"
        if self.source_file_type.isChecked():
            file_type = "*.docx"
        elif self.source_file_type_2.isChecked():
            file_type = "*.pdf"
        elif self.source_file_type_3.isChecked():
            file_type = "*.html"
        self.selected_dir = QFileDialog.getOpenFileNames(self, caption='选择文件', directory='', filter=file_type)
        self.file_conv_path.setText(';'.join(self.selected_dir[0]))
        # print(self.selected_dir)

    # 转换按钮
    def btn_conv(self):
        self.init_ui_text()
        # self.btn_file_conv.setDisabled(True)
        if self.file_conv_path.text() == "":
            QMessageBox.about(self, "提醒", "文件路径不能为空")
            return

        file_path_text = self.file_conv_path.text()
        self.file_conv_result_text.setPlainText("")
        self.file_conv_progress_bar.setValue(0)
        self.files = []
        # 如果是文件夹就遍历
        if os.path.isdir(file_path_text):
            file_type = ".docx"
            if self.source_file_type_2.isChecked():
                file_type = ".pdf"
            elif self.source_file_type_3.isChecked():
                file_type = ".html"
            self.files = file_util.file_list(file_path_text, file_type)
            if len(self.files) == 0:
                pass
        # 不是文件夹就是文件
        else:
            self.files = file_path_text.split(";")
        # 有可转换文件
        if len(self.files) > 0:
            try:
                self.file_conv_progress_bar.setMaximum(len(self.files))
                self.file_conv_progress_bar.show()
                for f in self.files:
                    print("start:" + f)
                    t = threading.Thread(self.converter(f))
                    t.start()
                    # t.join()
                while self.conv_count == len(self.files):
                    # print("转换结束，跳出循环")
                    break
            except Exception as e:
                print(e)
                self.done = " 转换失败"
                self.file_conv_result_text. \
                    setPlainText(self.file_conv_result_text.toPlainText() + f + self.done + "\r\n")
        # self.btn_file_conv.setDisabled(False)

    def converter(self, f):
        print('开始转换：' + f)
        time.sleep(1)
        # 转PDF
        if self.file_ext_select.currentIndex() == 0:
            # docx转PDF
            if self.source_file_type.isChecked():
                word.docx_to_pdf(f)
        # 转图片
        elif self.file_ext_select.currentIndex() == 1:
            # PDF转图片
            if self.source_file_type_2.isChecked():
                pdf.pdf_to_image(f)
            # docx转图片，先转成pdf，再转图片
            elif self.source_file_type.isChecked():
                pdf_name = word.docx_to_pdf(f)
                pdf.pdf_to_image(pdf_name)
                print(pdf_name)
                os.remove(pdf_name)
        # 转纯文本
        elif self.file_ext_select.currentIndex() == 2:
            if self.source_file_type.isChecked():
                word.docx_to_txt(f)
            elif self.source_file_type_2.isChecked():
                pdf.pdf_to_txt(f)
        # 转HTML
        elif self.file_ext_select.currentIndex() == 3:
            if self.source_file_type.isChecked():
                word.docx_to_html(f)
            elif self.source_file_type_2.isChecked():
                pdf.pdf_to_html(f)
        # 转docx
        elif self.file_ext_select.currentIndex() == 4:
            if self.source_file_type_2.isChecked():
                pdf.pdf_to_docx(f)
        self.conv_count += 1
        self.file_conv_progress_bar.setValue(self.conv_count)
        self.file_conv_result_text. \
            setPlainText(self.file_conv_result_text.toPlainText() + f + self.done + "\r\n")
        print('转换完成：' + f)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Run()
    ico_path = os.path.join(os.path.dirname(__file__), './resource/logo.ico')
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(ico_path), )
    ui.setWindowIcon(icon)
    ui.show()
    sys.exit(app.exec_())
