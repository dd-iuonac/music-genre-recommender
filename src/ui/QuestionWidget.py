# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\ui\QuestionWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_QuestionWidget(object):
    def setupUi(self, QuestionWidget):
        QuestionWidget.setObjectName("QuestionWidget")
        QuestionWidget.resize(498, 332)
        self.verticalLayout = QtWidgets.QVBoxLayout(QuestionWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_question = QtWidgets.QTextBrowser(QuestionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_question.sizePolicy().hasHeightForWidth())
        self.textBrowser_question.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textBrowser_question.setFont(font)
        self.textBrowser_question.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser_question.setObjectName("textBrowser_question")
        self.verticalLayout.addWidget(self.textBrowser_question)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(QuestionWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.comboBox_options = QtWidgets.QComboBox(QuestionWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_options.setFont(font)
        self.comboBox_options.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.comboBox_options.setObjectName("comboBox_options")
        self.verticalLayout_2.addWidget(self.comboBox_options)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_back = QtWidgets.QPushButton(QuestionWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.pushButton_next = QtWidgets.QPushButton(QuestionWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.pushButton_submit = QtWidgets.QPushButton(QuestionWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_submit.setObjectName("pushButton_submit")
        self.horizontalLayout.addWidget(self.pushButton_submit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QuestionWidget)
        QtCore.QMetaObject.connectSlotsByName(QuestionWidget)

    def retranslateUi(self, QuestionWidget):
        _translate = QtCore.QCoreApplication.translate
        QuestionWidget.setWindowTitle(_translate("QuestionWidget", "Form"))
        self.label.setText(_translate("QuestionWidget", "Answer:"))
        self.pushButton_back.setText(_translate("QuestionWidget", "Back"))
        self.pushButton_next.setText(_translate("QuestionWidget", "Next"))
        self.pushButton_submit.setText(_translate("QuestionWidget", "Submit"))
