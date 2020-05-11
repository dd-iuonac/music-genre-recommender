import os
import sys

from PySide2 import QtWidgets

from src.BlackPalette import BlackPalette
from src.InferenceMachine import InferenceMachine
from src.QuestionWidget import QuestionWidget
from src.ResultWidget import ResultWidget
from src.StartWidget import StartWidget
from src.ui.MainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, info_path, knowledge_base_path, qa_path):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.actionExit.triggered.connect(lambda: sys.exit(0))
        self.actionLoad_KnowledgeBase.triggered.connect(self.on_load_knowledge_base)
        self.actionLoad_Information.triggered.connect(self.on_load_information)
        self.actionLoad_Questions.triggered.connect(self.on_load_questions)
        self.actionRun.triggered.connect(self.on_action_run)
        self.actionAbout.triggered.connect(self.on_action_about)

        self.inferenceMachine: InferenceMachine = InferenceMachine()
        self.inferenceMachine.load_info_file(info_path)
        self.inferenceMachine.load_kb_file(knowledge_base_path)
        self.inferenceMachine.load_questions_file(qa_path)
        self.questionWidget: QuestionWidget = QuestionWidget()
        self.questionWidget.resultSignal.connect(self.on_finish)

        self.resultWidget: ResultWidget = ResultWidget()
        self.resultWidget.pushButton_reset.clicked.connect(self.on_reset)
        self.startWidget: StartWidget = StartWidget()
        self.startWidget.pushButton_start.clicked.connect(self.on_action_run)
        self.setCentralWidget(self.startWidget)

    def on_reset(self):
        self.startWidget = StartWidget()
        self.startWidget.pushButton_start.clicked.connect(self.on_action_run)
        self.setCentralWidget(self.startWidget)
        self.actionLoad_Information.setEnabled(True)
        self.actionLoad_KnowledgeBase.setEnabled(True)
        self.actionLoad_Questions.setEnabled(True)
        self.actionRun.setEnabled(True)

    def on_finish(self, result: dict):
        r = self.inferenceMachine.infer(result)
        self.resultWidget = ResultWidget()
        self.resultWidget.update_result(r, self.inferenceMachine.get_info_description(r))
        self.resultWidget.pushButton_reset.clicked.connect(self.on_reset)
        self.setCentralWidget(self.resultWidget)

    def on_action_about(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setStyleSheet("background-color: #000000; color: #ffffff; font-size: 12pt")
        msg.setPalette(BlackPalette())
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.setWindowTitle("About")
        msg.setText("This software is an expert system that recommends music.\n\nAuthors:\n\tDaniel-Domițian Iuonac\n\tFlavius-Denis Ilisie\n\n Copyright @ 2020")
        msg.show()

    def on_action_run(self):
        if not self.inferenceMachine.is_ready():
            msg = QtWidgets.QMessageBox(self)
            msg.setPalette(BlackPalette())
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setWindowTitle("Warning...")
            msg.setText("Inference Machine is not ready!\nPlease load all necessary files!")
            msg.show()
            return
        self.actionLoad_Information.setEnabled(False)
        self.actionLoad_KnowledgeBase.setEnabled(False)
        self.actionLoad_Questions.setEnabled(False)
        self.actionRun.setEnabled(False)
        self.questionWidget: QuestionWidget = QuestionWidget()
        self.questionWidget.resultSignal.connect(self.on_finish)
        self.setCentralWidget(self.questionWidget)
        self.questionWidget.load_questions(self.inferenceMachine.Questions)
        self.questionWidget.start()

    def on_load_questions(self):
        filename = self._select_file_dialog("Load Questions", "Json file (*.json)")
        if filename:
            if ".json" not in filename:
                filename += ".json"
            self.inferenceMachine.load_questions_file(filename)

    def on_load_information(self):
        filename = self._select_file_dialog("Load Information", "Json file (*.json)")
        if filename:
            if ".json" not in filename:
                filename += ".json"
            self.inferenceMachine.load_info_file(filename)

    def on_load_knowledge_base(self):
        filename = self._select_file_dialog("Load Knowledge Base", "Text file (*.txt)")
        if filename:
            if ".txt" not in filename:
                filename += ".txt"
            self.inferenceMachine.load_kb_file(filename)

    @staticmethod
    def _select_file_dialog(title: str, filter_type: str = "Text file (*.txt)"):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setPalette(BlackPalette())
        file_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        path = os.getcwd()
        file_path = file_dialog.getOpenFileName(QtWidgets.QWidget(), title, path, filter=filter_type,
                                                options=QtWidgets.QFileDialog.DontUseNativeDialog)
        filename = file_path[0]

        if filename:
            return filename
