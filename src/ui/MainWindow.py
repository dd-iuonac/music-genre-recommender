# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLoad_KnowledgeBase = QtWidgets.QAction(MainWindow)
        self.actionLoad_KnowledgeBase.setObjectName("actionLoad_KnowledgeBase")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_Questions = QtWidgets.QAction(MainWindow)
        self.actionLoad_Questions.setObjectName("actionLoad_Questions")
        self.actionLoad_Information = QtWidgets.QAction(MainWindow)
        self.actionLoad_Information.setObjectName("actionLoad_Information")
        self.menuFile.addAction(self.actionLoad_Information)
        self.menuFile.addAction(self.actionLoad_Questions)
        self.menuFile.addAction(self.actionLoad_KnowledgeBase)
        self.menuFile.addAction(self.actionExit)
        self.menuTool.addAction(self.actionRun)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad_KnowledgeBase.setText(_translate("MainWindow", "Load KnowledgeBase"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLoad_Questions.setText(_translate("MainWindow", "Load Questions"))
        self.actionLoad_Information.setText(_translate("MainWindow", "Load Information"))
