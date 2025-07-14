# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1022, 779)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1001, 731))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 270, 91, 41))
        self.id_input = QLineEdit(self.tab)
        self.id_input.setObjectName(u"id_input")
        self.id_input.setGeometry(QRect(150, 270, 181, 51))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 380, 91, 41))
        self.name_input = QLineEdit(self.tab)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(150, 380, 181, 51))
        self.status_label = QLabel(self.tab)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(470, 40, 461, 491))
        self.saveButton = QPushButton(self.tab)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(170, 550, 151, 61))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.camera_label = QLabel(self.tab_2)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setGeometry(QRect(490, 120, 471, 451))
        self.result_table = QTableWidget(self.tab_2)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setGeometry(QRect(40, 70, 361, 411))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 50, 131, 41))
        self.horizontalLayoutWidget = QWidget(self.tab_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(474, 520, 471, 171))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.openButton = QPushButton(self.horizontalLayoutWidget)
        self.openButton.setObjectName(u"openButton")

        self.horizontalLayout.addWidget(self.openButton)

        self.captureButton = QPushButton(self.horizontalLayoutWidget)
        self.captureButton.setObjectName(u"captureButton")

        self.horizontalLayout.addWidget(self.captureButton)

        self.trainButton = QPushButton(self.horizontalLayoutWidget)
        self.trainButton.setObjectName(u"trainButton")

        self.horizontalLayout.addWidget(self.trainButton)

        self.recognizeButton = QPushButton(self.horizontalLayoutWidget)
        self.recognizeButton.setObjectName(u"recognizeButton")

        self.horizontalLayout.addWidget(self.recognizeButton)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 20, 131, 31))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"id", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d", None))
        self.status_label.setText("")
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u4fe1\u606f\u5f55\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.camera_label.setText("")
        self.label_4.setText("")
        self.openButton.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.captureButton.setText(QCoreApplication.translate("Dialog", u"\u91c7\u96c6\u4eba\u8138\u6570\u636e", None))
        self.trainButton.setText(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u6a21\u578b", None))
        self.recognizeButton.setText(QCoreApplication.translate("Dialog", u"\u6253\u5361\u6210\u529f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6253\u5361\u8bb0\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
    # retranslateUi

