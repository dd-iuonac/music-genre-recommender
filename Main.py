import sys

from PySide2 import QtWidgets

from src.BlackPalette import BlackPalette
from src.MainWindow import MainWindow

INFORMATION = "se_music.xlsx"
# KNOWLEDGE_BASE = "music-if-then.txt"
KNOWLEDGE_BASE = "KnowledgeBase.txt"
QA = "QA.json"


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setPalette(BlackPalette())
    mainWindow = MainWindow(INFORMATION, KNOWLEDGE_BASE, QA)
    mainWindow.setPalette(BlackPalette())
    mainWindow.show()
    app.exec_()
