from PySide2 import QtWidgets

from src.BlackPalette import BlackPalette
from src.ui.ResultWidget import Ui_ResultWidget


class ResultWidget(Ui_ResultWidget, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ResultWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.setPalette(BlackPalette())

    def update_result(self, conclusion, text):
        self.textBrowser.setText(f"{conclusion}:\n\n{text}")
