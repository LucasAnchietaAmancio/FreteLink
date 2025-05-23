# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dash_sys_copy_new.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(850, 643)
        Form.setMinimumSize(QSize(850, 643))
        Form.setMaximumSize(QSize(850, 643))
        Form.setStyleSheet(u"#Form {\n"
"       background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #242A35,\n"
"        stop:1 #111213\n"
"    );\n"
"    border: 1.2px solid #2E2F31;\n"
"    border-radius: 10px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_14 = QFrame(Form)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.frame_14)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(280, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"/* Estilo geral do bot\u00e3o */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #a0a0a0;\n"
"    padding: 10px 20px;\n"
"    border: none;\n"
"    text-align: left;\n"
"    font-size: 14px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* \u00cdcone alinhado \u00e0 esquerda com texto */\n"
"QPushButton::icon {\n"
"    padding-right: 25px;\n"
"}\n"
"\n"
"/* Bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #242A35;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Bot\u00e3o selecionado (ativo) */\n"
"QPushButton:checked {\n"
"    background-color: rgba(45, 45, 45, 0.7); /* tamb\u00e9m transparente */\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/pasta-aberta.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"/* Estilo geral do bot\u00e3o */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #a0a0a0;\n"
"    padding: 10px 20px;\n"
"    border: none;\n"
"    text-align: left;\n"
"    font-size: 14px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* \u00cdcone alinhado \u00e0 esquerda com texto */\n"
"QPushButton::icon {\n"
"    padding-right: 25px;\n"
"}\n"
"\n"
"/* Bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #242A35;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Bot\u00e3o selecionado (ativo) */\n"
"QPushButton:checked {\n"
"    background-color: rgba(45, 45, 45, 0.7); /* tamb\u00e9m transparente */\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_4.setIcon(icon)

        self.verticalLayout_7.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"/* Estilo geral do bot\u00e3o */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: #a0a0a0;\n"
"    padding: 10px 20px;\n"
"    border: none;\n"
"    text-align: left;\n"
"    font-size: 14px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* \u00cdcone alinhado \u00e0 esquerda com texto */\n"
"QPushButton::icon {\n"
"    padding-right: 25px;\n"
"}\n"
"\n"
"/* Bot\u00e3o ao passar o mouse */\n"
"QPushButton:hover {\n"
"    background-color: #242A35;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Bot\u00e3o selecionado (ativo) */\n"
"QPushButton:checked {\n"
"    background-color: rgba(45, 45, 45, 0.7); /* tamb\u00e9m transparente */\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icons/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon1)

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_7.addWidget(self.label_7)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.Pagina = QStackedWidget(self.frame_14)
        self.Pagina.setObjectName(u"Pagina")
        self.Pagina.setStyleSheet(u"#page_11{\n"
" background-color: transparent\n"
"}\n"
"")
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_3 = QHBoxLayout(self.page_11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.page_11)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(390, 450))
        self.frame_3.setMaximumSize(QSize(1424664, 16777215))
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
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 45))
        self.frame_5.setStyleSheet(u"boder:none;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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
        self.frame_6.setMinimumSize(QSize(0, 320))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 10))
        font = QFont()
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label)

        self.dateEdit = QDateEdit(self.frame_6)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 40))
        self.dateEdit.setFont(font)
        self.dateEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"    border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #2E2F31;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(teamplates/icons/calendario.png);  /* Substitua pelo caminho do seu \u00edcone */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"")
        self.dateEdit.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout_4.addWidget(self.dateEdit)

        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 10))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_4.addWidget(self.label_2)

        self.dateEdit_2 = QDateEdit(self.frame_6)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setEnabled(True)
        self.dateEdit_2.setMaximumSize(QSize(16777214, 40))
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit_2.setStyleSheet(u"QDateEdit {\n"
"    border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #2E2F31;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(teamplates/icons/calendario.png);  /* Substitua pelo caminho do seu \u00edcone */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"")
        self.dateEdit_2.setDateTime(QDateTime(QDate(2025, 1, 31), QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)

        self.verticalLayout_4.addWidget(self.dateEdit_2)

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

        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"*{\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_4.addWidget(self.checkBox)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.progressBar = QProgressBar(self.frame_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 15))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: #1E1F21;\n"
"    border: 1px solid #444;\n"
"    border-radius: 6px;\n"
"    text-align: center;\n"
"    color: #CCCCCC;\n"
"border: 1px solid #29313C;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #3434CC;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.progressBar.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #AAAAAA;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_3)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 35))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #1F2123;\n"
"    color: #CFCFCF;\n"
"    font-weight: 600;\n"
"    border: 1px solid #2E2F31;\n"
"    border-radius: 8px;\n"
"    padding: 8px 0;\n"
"	border: 1px solid #29313C;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #292B2E;\n"
"    color: #FFFFFF;\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: #AAAAAA;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.Pagina.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.page_12.setStyleSheet(u"#page_12{\n"
" background-color: transparent\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.page_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.page_12)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4 {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #242A35,\n"
"        stop:1 #111213\n"
"    );\n"
"    border: 1.2px solid #2E2F31;\n"
"    border-radius: 10px;\n"
"border: 2px solid #29313C;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_59 = QLabel(self.frame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"* {\n"
"    color: #EEEEEE;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 1px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.label_59, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_49 = QFrame(self.frame_4)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_49)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_61 = QLabel(self.frame_49)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(0, 0))
        self.label_61.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_61)

        self.comboBox_7 = QComboBox(self.frame_49)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(0, 40))
        self.comboBox_7.setStyleSheet(u"* {\n"
"     border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(C:\\Users\\lucas\\Documents\\PROJETOS-CLEINTES\\THAYLLA KAUANI\\back-end\\sys_automation_cte\\teamplates\\icons\\seta.png);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border: none;\n"
"    background: transparent;\n"
"    padding-right: 10px;\n"
"}")

        self.verticalLayout_2.addWidget(self.comboBox_7)

        self.label_60 = QLabel(self.frame_49)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 40))
        self.label_60.setMaximumSize(QSize(16777215, 20))
        self.label_60.setFont(font)
        self.label_60.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_60)

        self.dateEdit_28 = QDateEdit(self.frame_49)
        self.dateEdit_28.setObjectName(u"dateEdit_28")
        self.dateEdit_28.setMinimumSize(QSize(0, 40))
        self.dateEdit_28.setFont(font)
        self.dateEdit_28.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit_28.setStyleSheet(u"QDateEdit {\n"
"    border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #2E2F31;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(teamplates/icons/calendario.png);  /* Substitua pelo caminho do seu \u00edcone */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"")
        self.dateEdit_28.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_28.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEdit_28)

        self.label_62 = QLabel(self.frame_49)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(0, 40))
        self.label_62.setMaximumSize(QSize(16777215, 20))
        self.label_62.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_62)

        self.dateEdit_27 = QDateEdit(self.frame_49)
        self.dateEdit_27.setObjectName(u"dateEdit_27")
        self.dateEdit_27.setEnabled(True)
        self.dateEdit_27.setMinimumSize(QSize(0, 40))
        self.dateEdit_27.setMaximumSize(QSize(16777214, 40))
        self.dateEdit_27.setFont(font)
        self.dateEdit_27.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit_27.setStyleSheet(u"QDateEdit {\n"
"    border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #2E2F31;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(teamplates/icons/calendario.png);  /* Substitua pelo caminho do seu \u00edcone */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"")
        self.dateEdit_27.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_27.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.dateEdit_27)

        self.horizontalSpacer_6 = QSpacerItem(483, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton_27 = QPushButton(self.frame_49)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(0, 45))
        self.pushButton_27.setFont(font1)
        self.pushButton_27.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_27.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.pushButton_27)


        self.verticalLayout.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frame_4)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_64 = QLabel(self.frame_50)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 40))
        self.label_64.setStyleSheet(u"QLabel {\n"
"    color: #AAAAAA;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.label_64)


        self.verticalLayout.addWidget(self.frame_50)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.Pagina.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setStyleSheet(u"#page_13{\n"
" background-color: transparent\n"
"}\n"
"")
        self.verticalLayout_72 = QVBoxLayout(self.page_13)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_51 = QFrame(self.page_13)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"#frame_51{\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #242A35,\n"
"        stop:1 #111213\n"
"    );\n"
"    border: 1.2px solid #2E2F31;\n"
"    border-radius: 10px;\n"
"border: 2px solid #29313C;\n"
"}")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_51)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.frame_59 = QFrame(self.frame_51)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_73 = QLabel(self.frame_59)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"* {\n"
"    color: #EEEEEE;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    letter-spacing: 1px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_73, 0, Qt.AlignHCenter)


        self.verticalLayout_70.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_51)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 450))
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_60)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_74 = QLabel(self.frame_60)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 40))
        self.label_74.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_71.addWidget(self.label_74)

        self.lineEdit = QLineEdit(self.frame_60)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
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

        self.verticalLayout_71.addWidget(self.lineEdit)

        self.label_5 = QLabel(self.frame_60)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 50))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_71.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.frame_60)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setStyleSheet(u"* {\n"
"     border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"")

        self.verticalLayout_71.addWidget(self.lineEdit_3)

        self.label_75 = QLabel(self.frame_60)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(0, 35))
        self.label_75.setMaximumSize(QSize(16777215, 20))
        self.label_75.setFont(font)
        self.label_75.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_71.addWidget(self.label_75)

        self.lineEdit_2 = QLineEdit(self.frame_60)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 40))
        self.lineEdit_2.setStyleSheet(u"* {\n"
"     border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"")

        self.verticalLayout_71.addWidget(self.lineEdit_2)

        self.label_76 = QLabel(self.frame_60)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(0, 40))
        self.label_76.setMaximumSize(QSize(16777215, 20))
        self.label_76.setStyleSheet(u"QLabel {\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")

        self.verticalLayout_71.addWidget(self.label_76)

        self.dateEdit_34 = QDateEdit(self.frame_60)
        self.dateEdit_34.setObjectName(u"dateEdit_34")
        self.dateEdit_34.setEnabled(True)
        self.dateEdit_34.setMinimumSize(QSize(0, 40))
        self.dateEdit_34.setMaximumSize(QSize(16777214, 40))
        self.dateEdit_34.setFont(font)
        self.dateEdit_34.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit_34.setStyleSheet(u"QDateEdit {\n"
"    border-radius: 6px;\n"
"    background-color: #242A35;\n"
"    color: white;\n"
"    border: 2px solid #29313C;\n"
"    padding-right: 24px; /* espa\u00e7o pro \u00edcone */\n"
"    padding-left: 14px;   /* espa\u00e7o pro texto */\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #2E2F31;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    image: url(teamplates/icons/calendario.png);  /* Substitua pelo caminho do seu \u00edcone */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"")
        self.dateEdit_34.setDateTime(QDateTime(QDate(1990, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_34.setCalendarPopup(True)

        self.verticalLayout_71.addWidget(self.dateEdit_34)

        self.horizontalSpacer_8 = QSpacerItem(415, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_71.addItem(self.horizontalSpacer_8)

        self.pushButton_31 = QPushButton(self.frame_60)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 45))
        self.pushButton_31.setFont(font1)
        self.pushButton_31.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_31.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_71.addWidget(self.pushButton_31)


        self.verticalLayout_70.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_51)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_77 = QLabel(self.frame_61)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(0, 40))
        self.label_77.setStyleSheet(u"QLabel {\n"
"    color: #AAAAAA;\n"
"    font-size: 13px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_77)


        self.verticalLayout_70.addWidget(self.frame_61)


        self.verticalLayout_72.addWidget(self.frame_51)

        self.Pagina.addWidget(self.page_13)

        self.horizontalLayout_2.addWidget(self.Pagina)


        self.horizontalLayout.addWidget(self.frame_14)


        self.retranslateUi(Form)

        self.Pagina.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Cte Automation", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u" Coleta de dados", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u" Fechamento", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u" Cadastro", None))
        self.label_7.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"COLETA DE DADOS", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data Inicial", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Data Final", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Buscar Dados", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"Validar Captcha", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Ultima Atualiza\u00e7\u00e3o:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Pr\u00f3xima Etapa", None))
        self.label_6.setText("")
        self.label_59.setText(QCoreApplication.translate("Form", u"FECHAMENTO POR MOTORISTA", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"Motorista", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"Data Inicial", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"Data Final", None))
        self.pushButton_27.setText(QCoreApplication.translate("Form", u"Gerar Relat\u00f3rio", None))
        self.label_64.setText("")
        self.label_73.setText(QCoreApplication.translate("Form", u"CADASTRO DE MOTORISTA", None))
        self.label_74.setText(QCoreApplication.translate("Form", u"Nome", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Digite o nome", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"C\u00f3digo do Motorista", None))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Digite o RNTRC", None))
        self.label_75.setText(QCoreApplication.translate("Form", u"CPF", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Digite o CPF", None))
        self.label_76.setText(QCoreApplication.translate("Form", u"Data de Nascimento", None))
        self.pushButton_31.setText(QCoreApplication.translate("Form", u"Cadastrar", None))
        self.label_77.setText("")
    # retranslateUi

