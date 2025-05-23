# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dash_sys_licence.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 500)
        Form.setMinimumSize(QSize(450, 500))
        Form.setMaximumSize(QSize(450, 500))
        Form.setStyleSheet(u"#Form {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #242A35,\n"
"        stop:1 #111213\n"
"    );\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(390, 0))
        self.frame_3.setMaximumSize(QSize(450, 16777215))
        self.frame_3.setStyleSheet(u"#frame_3 {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #242A35,\n"
"        stop:1 #111213\n"
"    );\n"
"    border: 1.2px solid #2E2F31;\n"
"    border-radius: 10px;\n"
"border: 2px solid #29313C;\n"
"}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 45))
        self.frame_5.setStyleSheet(u"boder:none;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"* {\n"
"    color: #EEEEEE;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 1px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 260))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 10))
        font = QFont()
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setStyleSheet(u"* {\n"
"     border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #5859B5,\n"
"        stop:1 #3435C9\n"
"    );\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 0;\n"
"border: 1px solid #29313C;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #6E70F4,\n"
"        stop:1 #5D5FEF\n"
"    );\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Frete Link", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"VALIDAR SUA LICEN\u00c7A", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Insira seu c\u00f3digo de verifica\u00e7\u00e3o", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Digite o c\u00f3digo", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Buscar Dados", None))
    # retranslateUi

