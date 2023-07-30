# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionFullscreen = QAction(MainWindow)
        self.actionFullscreen.setObjectName(u"actionFullscreen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblTextEdit = QLabel(self.centralwidget)
        self.lblTextEdit.setObjectName(u"lblTextEdit")
        self.lblTextEdit.setGeometry(QRect(70, 20, 91, 20))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(170, 10, 241, 31))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(170, 50, 241, 31))
        self.lblPlainTextEdit = QLabel(self.centralwidget)
        self.lblPlainTextEdit.setObjectName(u"lblPlainTextEdit")
        self.lblPlainTextEdit.setGeometry(QRect(70, 60, 91, 20))
        self.btnTextEdit = QPushButton(self.centralwidget)
        self.btnTextEdit.setObjectName(u"btnTextEdit")
        self.btnTextEdit.setGeometry(QRect(440, 10, 81, 31))
        self.btnPlainTextEdit = QPushButton(self.centralwidget)
        self.btnPlainTextEdit.setObjectName(u"btnPlainTextEdit")
        self.btnPlainTextEdit.setGeometry(QRect(440, 50, 81, 31))
        self.lvModel = QListView(self.centralwidget)
        self.lvModel.setObjectName(u"lvModel")
        self.lvModel.setGeometry(QRect(10, 160, 371, 192))
        self.tblModel = QTableView(self.centralwidget)
        self.tblModel.setObjectName(u"tblModel")
        self.tblModel.setGeometry(QRect(410, 160, 371, 192))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 131, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(410, 140, 101, 16))
        self.btnSelectListViewModel = QPushButton(self.centralwidget)
        self.btnSelectListViewModel.setObjectName(u"btnSelectListViewModel")
        self.btnSelectListViewModel.setGeometry(QRect(300, 360, 80, 30))
        self.btnSelectTableViewModel = QPushButton(self.centralwidget)
        self.btnSelectTableViewModel.setObjectName(u"btnSelectTableViewModel")
        self.btnSelectTableViewModel.setGeometry(QRect(700, 360, 75, 30))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 89, 241, 31))
        self.lblLineEdit = QLabel(self.centralwidget)
        self.lblLineEdit.setObjectName(u"lblLineEdit")
        self.lblLineEdit.setGeometry(QRect(70, 100, 91, 20))
        self.btnLineEdit = QPushButton(self.centralwidget)
        self.btnLineEdit.setObjectName(u"btnLineEdit")
        self.btnLineEdit.setGeometry(QRect(440, 90, 81, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.actionFullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
#if QT_CONFIG(shortcut)
        self.actionFullscreen.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.lblTextEdit.setText(QCoreApplication.translate("MainWindow", u"Text Edit", None))
        self.lblPlainTextEdit.setText(QCoreApplication.translate("MainWindow", u"Plain Text Edit", None))
        self.btnTextEdit.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btnPlainTextEdit.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ListView (Model)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TableView (Model)", None))
        self.btnSelectListViewModel.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.btnSelectTableViewModel.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.lblLineEdit.setText(QCoreApplication.translate("MainWindow", u"Line Edit", None))
        self.btnLineEdit.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

