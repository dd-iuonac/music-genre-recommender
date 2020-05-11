# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\ResultWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ResultWidget(object):
    def setupUi(self, ResultWidget):
        ResultWidget.setObjectName("ResultWidget")
        ResultWidget.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(ResultWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(ResultWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_2.addWidget(self.textBrowser)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 95, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_reset = QtWidgets.QPushButton(ResultWidget)
        self.pushButton_reset.setMinimumSize(QtCore.QSize(200, 100))
        self.pushButton_reset.setMaximumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_reset.setFont(font)
        self.pushButton_reset.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.horizontalLayout.addWidget(self.pushButton_reset)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(ResultWidget)
        QtCore.QMetaObject.connectSlotsByName(ResultWidget)

    def retranslateUi(self, ResultWidget):
        _translate = QtCore.QCoreApplication.translate
        ResultWidget.setWindowTitle(_translate("ResultWidget", "Form"))
        self.pushButton_reset.setText(_translate("ResultWidget", "RESET"))
