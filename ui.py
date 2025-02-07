# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(990, 724)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainPage.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(MainPage)
        self.gridLayout.setObjectName("gridLayout")
        self.tab_main = QtWidgets.QTabWidget(MainPage)
        self.tab_main.setObjectName("tab_main")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 10, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.source_file_type_select = QtWidgets.QComboBox(self.tab)
        self.source_file_type_select.setMinimumSize(QtCore.QSize(0, 30))
        self.source_file_type_select.setObjectName("source_file_type_select")
        self.horizontalLayout_2.addWidget(self.source_file_type_select)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
        self.btn_file_con_select = QtWidgets.QPushButton(self.tab)
        self.btn_file_con_select.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_file_con_select.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_file_con_select.setFont(font)
        self.btn_file_con_select.setObjectName("btn_file_con_select")
        self.gridLayout_3.addWidget(self.btn_file_con_select, 2, 2, 1, 1)
        self.file_conv_path = QtWidgets.QLineEdit(self.tab)
        self.file_conv_path.setMinimumSize(QtCore.QSize(0, 30))
        self.file_conv_path.setObjectName("file_conv_path")
        self.gridLayout_3.addWidget(self.file_conv_path, 2, 1, 1, 1)
        self.file_conv_result_text = QtWidgets.QTextEdit(self.tab)
        self.file_conv_result_text.setObjectName("file_conv_result_text")
        self.gridLayout_3.addWidget(self.file_conv_result_text, 11, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setMinimumSize(QtCore.QSize(0, 50))
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMinimumSize(QtCore.QSize(0, 50))
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.file_conv_progress_bar = QtWidgets.QProgressBar(self.tab)
        self.file_conv_progress_bar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.file_conv_progress_bar.setFont(font)
        self.file_conv_progress_bar.setProperty("value", 0)
        self.file_conv_progress_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.file_conv_progress_bar.setObjectName("file_conv_progress_bar")
        self.gridLayout_3.addWidget(self.file_conv_progress_bar, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.btn_file_conv = QtWidgets.QPushButton(self.tab)
        self.btn_file_conv.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_file_conv.setObjectName("btn_file_conv")
        self.gridLayout_3.addWidget(self.btn_file_conv, 4, 1, 1, 1)
        self.target_file_type_select = QtWidgets.QComboBox(self.tab)
        self.target_file_type_select.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.target_file_type_select.setFont(font)
        self.target_file_type_select.setCurrentText("")
        self.target_file_type_select.setObjectName("target_file_type_select")
        self.gridLayout_3.addWidget(self.target_file_type_select, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setMinimumSize(QtCore.QSize(0, 40))
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tab1_txt_file_save_directory = QtWidgets.QLineEdit(self.tab)
        self.tab1_txt_file_save_directory.setMinimumSize(QtCore.QSize(0, 30))
        self.tab1_txt_file_save_directory.setObjectName("tab1_txt_file_save_directory")
        self.gridLayout_3.addWidget(self.tab1_txt_file_save_directory, 3, 1, 1, 1)
        self.tab1_btn_file_conv_save_directory = QtWidgets.QPushButton(self.tab)
        self.tab1_btn_file_conv_save_directory.setMinimumSize(QtCore.QSize(0, 30))
        self.tab1_btn_file_conv_save_directory.setObjectName("tab1_btn_file_conv_save_directory")
        self.gridLayout_3.addWidget(self.tab1_btn_file_conv_save_directory, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tab_main.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.tab3_combox_select_disk = QtWidgets.QComboBox(self.tab_3)
        self.tab3_combox_select_disk.setMinimumSize(QtCore.QSize(0, 30))
        self.tab3_combox_select_disk.setObjectName("tab3_combox_select_disk")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tab3_combox_select_disk)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.tab3_checkbox_scan_all_disk = QtWidgets.QCheckBox(self.tab_3)
        self.tab3_checkbox_scan_all_disk.setObjectName("tab3_checkbox_scan_all_disk")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tab3_checkbox_scan_all_disk)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.tab3_btn_scan = QtWidgets.QPushButton(self.tab_3)
        self.tab3_btn_scan.setMinimumSize(QtCore.QSize(0, 40))
        self.tab3_btn_scan.setObjectName("tab3_btn_scan")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tab3_btn_scan)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setMinimumSize(QtCore.QSize(0, 30))
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.tab_scan_result = QtWidgets.QTabWidget(self.tab_3)
        self.tab_scan_result.setObjectName("tab_scan_result")
        self.tab_scan_file_list = QtWidgets.QWidget()
        self.tab_scan_file_list.setObjectName("tab_scan_file_list")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_scan_file_list)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tab3_table_scan_files = QtWidgets.QTableWidget(self.tab_scan_file_list)
        self.tab3_table_scan_files.setMinimumSize(QtCore.QSize(0, 0))
        self.tab3_table_scan_files.setObjectName("tab3_table_scan_files")
        self.tab3_table_scan_files.setColumnCount(1)
        self.tab3_table_scan_files.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab3_table_scan_files.setHorizontalHeaderItem(0, item)
        self.gridLayout_5.addWidget(self.tab3_table_scan_files, 0, 0, 1, 1)
        self.tab_scan_result.addTab(self.tab_scan_file_list, "")
        self.tab_parser_keyword = QtWidgets.QWidget()
        self.tab_parser_keyword.setObjectName("tab_parser_keyword")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_parser_keyword)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tab3_table_parser_files = QtWidgets.QTableWidget(self.tab_parser_keyword)
        self.tab3_table_parser_files.setObjectName("tab3_table_parser_files")
        self.tab3_table_parser_files.setColumnCount(3)
        self.tab3_table_parser_files.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab3_table_parser_files.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab3_table_parser_files.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab3_table_parser_files.setHorizontalHeaderItem(2, item)
        self.gridLayout_7.addWidget(self.tab3_table_parser_files, 0, 0, 1, 1)
        self.tab_scan_result.addTab(self.tab_parser_keyword, "")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tab_scan_result)
        self.tab3_text_keywords = QtWidgets.QPlainTextEdit(self.tab_3)
        self.tab3_text_keywords.setMaximumSize(QtCore.QSize(16777215, 60))
        self.tab3_text_keywords.setObjectName("tab3_text_keywords")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tab3_text_keywords)
        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)
        self.tab_main.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tab2_txt_web_pages = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_txt_web_pages.setMinimumSize(QtCore.QSize(0, 30))
        self.tab2_txt_web_pages.setText("")
        self.tab2_txt_web_pages.setObjectName("tab2_txt_web_pages")
        self.gridLayout_2.addWidget(self.tab2_txt_web_pages, 3, 1, 1, 1)
        self.tab2_text_content = QtWidgets.QTextEdit(self.tab_2)
        self.tab2_text_content.setObjectName("tab2_text_content")
        self.gridLayout_2.addWidget(self.tab2_text_content, 5, 1, 1, 1)
        self.tab2_btn_get_web_site_content = QtWidgets.QPushButton(self.tab_2)
        self.tab2_btn_get_web_site_content.setMinimumSize(QtCore.QSize(0, 40))
        self.tab2_btn_get_web_site_content.setObjectName("tab2_btn_get_web_site_content")
        self.gridLayout_2.addWidget(self.tab2_btn_get_web_site_content, 4, 1, 1, 1)
        self.tab2_txt_web_tag = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_txt_web_tag.setMinimumSize(QtCore.QSize(0, 30))
        self.tab2_txt_web_tag.setObjectName("tab2_txt_web_tag")
        self.gridLayout_2.addWidget(self.tab2_txt_web_tag, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.tab2_txt_web_url = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_txt_web_url.setMinimumSize(QtCore.QSize(0, 30))
        self.tab2_txt_web_url.setText("")
        self.tab2_txt_web_url.setObjectName("tab2_txt_web_url")
        self.gridLayout_2.addWidget(self.tab2_txt_web_url, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.tab2_txt_key = QtWidgets.QLineEdit(self.tab_2)
        self.tab2_txt_key.setMinimumSize(QtCore.QSize(0, 30))
        self.tab2_txt_key.setText("")
        self.tab2_txt_key.setObjectName("tab2_txt_key")
        self.gridLayout_2.addWidget(self.tab2_txt_key, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tab_main.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tab_main, 0, 0, 1, 1)

        self.retranslateUi(MainPage)
        self.tab_main.setCurrentIndex(2)
        self.tab_scan_result.setCurrentIndex(0)
        self.btn_file_con_select.clicked.connect(MainPage.btn_select_file) # type: ignore
        self.btn_file_conv.clicked.connect(MainPage.btn_conv) # type: ignore
        self.tab2_btn_get_web_site_content.clicked.connect(MainPage.parser_web_site_content) # type: ignore
        self.source_file_type_select.currentIndexChanged['int'].connect(MainPage.target_file_type_select_change) # type: ignore
        self.tab1_btn_file_conv_save_directory.clicked.connect(MainPage.file_conv_select_save_directory) # type: ignore
        self.tab_main.currentChanged['int'].connect(MainPage.tab_change) # type: ignore
        self.tab3_btn_scan.clicked.connect(MainPage.scan_disk) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "小工具"))
        self.label_3.setText(_translate("MainPage", "转换结果"))
        self.btn_file_con_select.setText(_translate("MainPage", "选择文件或文件夹"))
        self.label_7.setText(_translate("MainPage", "源文件路径"))
        self.label_5.setText(_translate("MainPage", "目标文件格式"))
        self.label_8.setText(_translate("MainPage", "源文件格式"))
        self.btn_file_conv.setText(_translate("MainPage", "开始转换"))
        self.label_15.setText(_translate("MainPage", "保存路径"))
        self.tab1_txt_file_save_directory.setPlaceholderText(_translate("MainPage", "默认为文件所在目录"))
        self.tab1_btn_file_conv_save_directory.setText(_translate("MainPage", "选择文件夹"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab), _translate("MainPage", "文件转换"))
        self.label_10.setText(_translate("MainPage", "选择磁盘"))
        self.tab3_checkbox_scan_all_disk.setText(_translate("MainPage", "全盘扫描"))
        self.tab3_btn_scan.setText(_translate("MainPage", "开始扫描"))
        self.label_13.setText(_translate("MainPage", "扫描结果"))
        self.label_14.setText(_translate("MainPage", "关键字"))
        item = self.tab3_table_scan_files.horizontalHeaderItem(0)
        item.setText(_translate("MainPage", "文件名"))
        self.tab_scan_result.setTabText(self.tab_scan_result.indexOf(self.tab_scan_file_list), _translate("MainPage", "扫描到的文件"))
        item = self.tab3_table_parser_files.horizontalHeaderItem(0)
        item.setText(_translate("MainPage", "文件名"))
        item = self.tab3_table_parser_files.horizontalHeaderItem(1)
        item.setText(_translate("MainPage", "关键字"))
        item = self.tab3_table_parser_files.horizontalHeaderItem(2)
        item.setText(_translate("MainPage", "上下文"))
        self.tab_scan_result.setTabText(self.tab_scan_result.indexOf(self.tab_parser_keyword), _translate("MainPage", "包含关键字文件数量"))
        self.tab3_text_keywords.setPlainText(_translate("MainPage", "舆情 西藏 网络舆情 新疆棉"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_3), _translate("MainPage", "关键字扫描"))
        self.tab2_btn_get_web_site_content.setText(_translate("MainPage", "获取内容"))
        self.tab2_txt_web_tag.setPlaceholderText(_translate("MainPage", "标签用,分割"))
        self.label_4.setText(_translate("MainPage", "分页设置"))
        self.label_2.setText(_translate("MainPage", "网页地址"))
        self.label.setText(_translate("MainPage", "解析标签"))
        self.label_9.setText(_translate("MainPage", "关键地址"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.tab_2), _translate("MainPage", "政府网站工作简化"))
