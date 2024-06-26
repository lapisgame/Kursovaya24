# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SandboxButton = QtWidgets.QPushButton(self.centralwidget)
        self.SandboxButton.setGeometry(QtCore.QRect(790, 280, 191, 91))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.SandboxButton.setFont(font)
        self.SandboxButton.setObjectName("SandboxButton")
        self.AboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutButton.setGeometry(QtCore.QRect(10, 740, 131, 41))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.AboutButton.setFont(font)
        self.AboutButton.setObjectName("AboutButton")
        self.MainLabel = QtWidgets.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(30, 10, 381, 91))
        font = QtGui.QFont()
        font.setFamily("Lumberjack")
        font.setPointSize(32)
        self.MainLabel.setFont(font)
        self.MainLabel.setStyleSheet("color: black;")
        self.MainLabel.setObjectName("MainLabel")
        self.LectureButton = QtWidgets.QPushButton(self.centralwidget)
        self.LectureButton.setGeometry(QtCore.QRect(190, 280, 191, 91))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.LectureButton.setFont(font)
        self.LectureButton.setStyleSheet("")
        self.LectureButton.setObjectName("LectureButton")
        self.SettingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(1010, 740, 131, 41))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(14)
        self.SettingsButton.setFont(font)
        self.SettingsButton.setObjectName("SettingsButton")
        self.TaskButton = QtWidgets.QPushButton(self.centralwidget)
        self.TaskButton.setGeometry(QtCore.QRect(500, 280, 191, 91))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(16)
        self.TaskButton.setFont(font)
        self.TaskButton.setObjectName("TaskButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SandboxButton.setText(_translate("MainWindow", "Песочница"))
        self.AboutButton.setText(_translate("MainWindow", "О программе"))
        self.MainLabel.setText(_translate("MainWindow", "Lapis\\Learn\\Python"))
        self.LectureButton.setText(_translate("MainWindow", "Лекции"))
        self.SettingsButton.setText(_translate("MainWindow", "Настройки"))
        self.TaskButton.setText(_translate("MainWindow", "Задачи"))
