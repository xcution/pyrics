# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txLyrics = QtWidgets.QTextEdit(self.centralwidget)
        self.txLyrics.setReadOnly(True)
        self.txLyrics.setObjectName("txLyrics")
        self.verticalLayout.addWidget(self.txLyrics)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLoad_Lyrics = QtWidgets.QAction(MainWindow)
        self.actionLoad_Lyrics.setObjectName("actionLoad_Lyrics")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLyric_source = QtWidgets.QAction(MainWindow)
        self.actionLyric_source.setObjectName("actionLyric_source")
        self.toolBar.addAction(self.actionLoad_Lyrics)
        self.toolBar.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qpyrics"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuAbout.setTitle(_translate("MainWindow", "&Help"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.actionLoad_Lyrics.setText(_translate("MainWindow", "Load lyrics"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLyric_source.setText(_translate("MainWindow", "Lyric source"))

