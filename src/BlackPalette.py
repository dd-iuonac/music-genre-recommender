from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor


class BlackPalette(QPalette):
    def __init__(self):
        super(BlackPalette, self).__init__()
        self.setColor(QPalette.Window, QColor(53, 53, 53))
        self.setColor(QPalette.WindowText, Qt.white)
        self.setColor(QPalette.Base, QColor(15, 15, 15))
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, Qt.black)
        self.setColor(QPalette.ToolTipText, Qt.lightGray)
        self.setColor(QPalette.Text, Qt.lightGray)
        self.setColor(QPalette.Button, QColor(0, 0, 0))
        self.setColor(QPalette.ButtonText, Qt.white)
        self.setColor(QPalette.BrightText, Qt.red)
        self.setColor(QPalette.Highlight, QColor(255, 204, 0))
        self.setColor(QPalette.HighlightedText, Qt.black)
        self.setColor(QPalette.Midlight, QColor(203, 203, 203))
        self.setColor(QPalette.Mid, QColor(184, 184, 184))
        self.setColor(QPalette.Dark, QColor(159, 159, 159))
        self.setColor(QPalette.Shadow, QColor(118, 118, 118))
        self.setColor(QPalette.Light, Qt.white)
