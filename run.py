import os

from common import file_util, constant
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ui import Ui_MainPage


class Run(QtWidgets.QWidget, Ui_MainPage):
    def __init__(self):
        super(Run, self).__init__()
        self.setupUi(self)
        self.selected_dir = []
        self.save_dir = ''
        self.files = []
        self.file_conv_progress_bar.hide()
        self.conv_count = 0
        self.init_file_type_select()

    def init_ui_text(self):
        self.selected_dir = []
        self.files = []
        self.conv_count = 0

    def init_file_type_select(self):
        for key in constant.source_file_type.keys():
            self.source_file_type_select.addItem(constant.source_file_type[key], key)

    def target_file_type_select_change(self):
        self.target_file_type_select.clear()
        target_key = constant.get_can_convert_file_type(self.source_file_type_select.currentData())
        for key in target_key:
            self.target_file_type_select.addItem(constant.file_type[key], key)

    # 文件选择按钮
    def btn_select_file(self):
        # self.selected_dir = QFileDialog.getExistingDirectory(self, caption='选择文件夹', directory=os.getcwd())
        file_type = "*." + self.source_file_type_select.currentData()
        if self.source_file_type_select.currentData() == "image":
            file_type = "*.jpg;*.jpeg;*.png"
        root = 'C:/Users/jerry/Documents/'
        self.selected_dir = QFileDialog.getOpenFileNames(self, caption='选择文件', directory=root, filter=file_type)
        self.file_conv_path.setText(';'.join(self.selected_dir[0]))
        # print(self.selected_dir)

    # 选择转换后保存目录
    def file_conv_select_save_directory(self):
        self.save_dir = QFileDialog.getExistingDirectory(self, caption='选择转换保存文件夹', directory="")
        self.tab1_txt_file_save_directory.setText(self.save_dir)

    # 转换按钮
    def btn_conv(self):
        if self.file_conv_path.text() == "":
            QMessageBox.about(self, "提醒", "文件路径不能为空")
            return
        out_put_dir = self.tab1_txt_file_save_directory.text()
        if not file_util.is_dir(out_put_dir):
            QMessageBox.about(self, "提醒", "文件转换后保存路径不能为空并真实存在")
            return
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
            if len(self.files) == 0:
                pass
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
                        self.converter(f, out_put_dir)
                while self.conv_count == len(self.files):
                    print("转换结束，跳出循环")
                    break
            except Exception as e:
                print(e)
                self.file_conv_result_text. \
                    setPlainText(self.file_conv_result_text.toPlainText() + log_file_name + " 转换失败。" + "\r\n")
        # self.btn_file_conv.setDisabled(False)

    def converter(self, f, out_put_dir):
        from fileconv.factory import ConverterFactory
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
        self.file_conv_result_text. \
            setPlainText(self.file_conv_result_text.toPlainText() + log_file_name
                         + " 转换为" + self.target_file_type_select.currentText() + "成功。\r\n")

    def parser_web_site_content(self):
        from web import parser_gov
        try:
            content = parser_gov.parser(self.tab2_txt_web_url.text(), self.tab2_txt_key.text())
            for i in range(2, 22):
                url = self.tab2_txt_web_pages.text().format(str(i))
                print(url)
                content += parser_gov.parser(url, self.tab2_txt_key.text())
            self.tab2_text_content.setPlainText(content)
        except Exception as e:
            print(e)


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
