# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hely\he\Pyprojects\Jacquard_SRC\UItest_2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class TestUI(QtGui.QMainWindow):
    def __init__(self):
        super(TestUI, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1516, 987)
        MainWindow.setMinimumSize(QtCore.QSize(0, 80))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.top_text = QtGui.QLabel(self.centralwidget)
        self.top_text.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(36)
        self.top_text.setFont(font)
        self.top_text.setStyleSheet(_fromUtf8("background-color:rgb(0,0,255);\n"
"color:rgb(255,255,255)"))
        self.top_text.setAlignment(QtCore.Qt.AlignCenter)
        self.top_text.setObjectName(_fromUtf8("top_text"))
        self.gridLayout_3.addWidget(self.top_text, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.table_test_items = QtGui.QTableView(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table_test_items.sizePolicy().hasHeightForWidth())
        self.table_test_items.setSizePolicy(sizePolicy)
        self.table_test_items.setMinimumSize(QtCore.QSize(0, 100))
        self.table_test_items.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.table_test_items.setFont(font)
        self.table_test_items.setShowGrid(True)
        self.table_test_items.setObjectName(_fromUtf8("table_test_items"))
        self.gridLayout_2.addWidget(self.table_test_items, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setStyleSheet(_fromUtf8(""))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.sn1 = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.sn1.setFont(font)
        self.sn1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sn1.setObjectName(_fromUtf8("sn1"))
        self.horizontalLayout.addWidget(self.sn1)
        self.linesn1 = QtGui.QLineEdit(self.widget_2)
        self.linesn1.setMaximumSize(QtCore.QSize(200, 16777215))
        self.linesn1.setObjectName(_fromUtf8("linesn1"))
        self.horizontalLayout.addWidget(self.linesn1)
        self.time1 = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.time1.setFont(font)
        self.time1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time1.setObjectName(_fromUtf8("time1"))
        self.horizontalLayout.addWidget(self.time1)
        self.linetime1 = QtGui.QLineEdit(self.widget_2)
        self.linetime1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.linetime1.setText(_fromUtf8(""))
        self.linetime1.setObjectName(_fromUtf8("linetime1"))
        self.horizontalLayout.addWidget(self.linetime1)
        self.start = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy)
        self.start.setMinimumSize(QtCore.QSize(100, 50))
        self.start.setMaximumSize(QtCore.QSize(200, 50))
        self.start.setStyleSheet(_fromUtf8(""))
        self.start.setObjectName(_fromUtf8("start"))
        self.horizontalLayout.addWidget(self.start)
        self.reset = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        self.reset.setMinimumSize(QtCore.QSize(100, 50))
        self.reset.setMaximumSize(QtCore.QSize(200, 50))
        self.reset.setStyleSheet(_fromUtf8(""))
        self.reset.setObjectName(_fromUtf8("reset"))
        self.horizontalLayout.addWidget(self.reset)
        self.btn_exit = QtGui.QPushButton(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_exit.setMaximumSize(QtCore.QSize(200, 50))
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout.addWidget(self.btn_exit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.lab_result = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_result.sizePolicy().hasHeightForWidth())
        self.lab_result.setSizePolicy(sizePolicy)
        self.lab_result.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lab_result.setFont(font)
        self.lab_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_result.setObjectName(_fromUtf8("lab_result"))
        self.gridLayout.addWidget(self.lab_result, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_touchview = QtGui.QWidget()
        self.tab_touchview.setObjectName(_fromUtf8("tab_touchview"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_touchview)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.grid_touchview = QtGui.QGridLayout()
        self.grid_touchview.setSpacing(0)
        self.grid_touchview.setObjectName(_fromUtf8("grid_touchview"))
        self.gridLayout_6.addLayout(self.grid_touchview, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_touchview, _fromUtf8(""))
        self.tab_message = QtGui.QWidget()
        self.tab_message.setObjectName(_fromUtf8("tab_message"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_message)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.message = QtGui.QTextEdit(self.tab_message)
        self.message.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.message.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color:rgb(0,255,0);"))
        self.message.setObjectName(_fromUtf8("message"))
        self.gridLayout_4.addWidget(self.message, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_message, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 5)
        self.gridLayout_3.setRowStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1516, 37))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setStyleSheet(_fromUtf8("background-color: rgb(188, 188, 188);\n"
"color:rgb(0,0,0)"))
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.top_text.setText(_translate("MainWindow", "KML Tester V1.0.0.0", None))
        self.sn1.setText(_translate("MainWindow", "SN", None))
        self.time1.setText(_translate("MainWindow", "Time", None))
        self.start.setText(_translate("MainWindow", "Start", None))
        self.reset.setText(_translate("MainWindow", "Reset", None))
        self.btn_exit.setText(_translate("MainWindow", "exit", None))
        self.lab_result.setText(_translate("MainWindow", "IDLE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_touchview), _translate("MainWindow", "touch view", None))
        self.message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:12pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_message), _translate("MainWindow", "message", None))

