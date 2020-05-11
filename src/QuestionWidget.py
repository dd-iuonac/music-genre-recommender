from PySide2 import QtWidgets, QtCore

from src.BlackPalette import BlackPalette
from src.model.Question import Question
from src.ui.QuestionWidget import Ui_QuestionWidget


class QuestionWidget(Ui_QuestionWidget, QtWidgets.QWidget):
    resultSignal = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(QuestionWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.setPalette(BlackPalette())
        self.questions = None
        self.result = None
        self.currentQuestion = 0
        self.optionsWidgets = []
        self.pushButton_back.clicked.connect(self.on_button_back)
        self.pushButton_next.clicked.connect(self.on_button_next)
        self.pushButton_submit.clicked.connect(self.on_button_submit)

    def load_questions(self, questions: dict):
        self.questions = questions

    def on_button_back(self, value):
        if self.currentQuestion - 1 >= 0:
            self.currentQuestion -= 1
            self.update_ui(self.questions[self.currentQuestion])

        self.pushButton_submit.setVisible(False)
        self.pushButton_next.setVisible(True)
        if self.currentQuestion == 0:
            self.pushButton_back.setVisible(False)

    def on_button_next(self, value):
        self.pushButton_back.setVisible(True)
        self.result[self.questions[self.currentQuestion].category] = self.comboBox_options.currentIndex()
        self.currentQuestion += 1
        question = self.questions[self.currentQuestion]
        self.update_ui(question)
        if self.currentQuestion + 1 == len(self.questions):
            self.pushButton_next.setVisible(False)
            self.pushButton_submit.setVisible(True)
            self.result[self.questions[self.currentQuestion].category] = self.comboBox_options.currentIndex()

    def on_button_submit(self, value):
        self.resultSignal.emit(self.result)

    def start(self):
        self.result = {}
        self.pushButton_submit.setVisible(False)
        self.pushButton_back.setVisible(False)
        self.currentQuestion = 0
        question = self.questions[self.currentQuestion]
        self.update_ui(question)

    def update_ui(self, question: Question):
        self.textBrowser_question.setText(f"Q_{self.currentQuestion + 1}. {question.text}")
        self.comboBox_options.clear()
        for option in question.options:
            self.comboBox_options.addItem(option)
        try:
            self.comboBox_options.setCurrentIndex(int(self.result[question.category]))
        except KeyError:
            self.comboBox_options.setCurrentIndex(0)

        # for w in self.optionsWidgets:
        #     self.groupBox_options.layout().removeWidget(w)
        # self.optionsWidgets.clear()
        #
        # for option in question.options:
        #     radio_button = QtWidgets.QRadioButton(text=str(option))
        #     self.groupBox_options.layout().addWidget(radio_button)

