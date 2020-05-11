from PySide2 import QtWidgets

from src.BlackPalette import BlackPalette
from .ui.StartWidget import Ui_StartWidget


class StartWidget(Ui_StartWidget, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StartWidget, self).__init__(parent=parent)
        self.setupUi(self)
        self.setPalette(BlackPalette())

        self.textBrowser.setText("This Expert system will recommend music genre based on a variety of specific desired attributes.")