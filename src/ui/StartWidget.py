# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\StartWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_StartWidget(object):
    def setupUi(self, StartWidget):
        StartWidget.setObjectName("StartWidget")
        StartWidget.resize(709, 655)
        self.verticalLayout = QtWidgets.QVBoxLayout(StartWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(StartWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem = QtWidgets.QSpacerItem(20, 298, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_start = QtWidgets.QPushButton(StartWidget)
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButton_start.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(StartWidget)
        QtCore.QMetaObject.connectSlotsByName(StartWidget)

    def retranslateUi(self, StartWidget):
        _translate = QtCore.QCoreApplication.translate
        StartWidget.setWindowTitle(_translate("StartWidget", "Form"))
        self.pushButton_start.setText(_translate("StartWidget", "START"))
import resources_rc
