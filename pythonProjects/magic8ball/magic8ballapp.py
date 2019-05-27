from PyQt5.QtWidgets import QApplication

class Magic8BallApp(QApplication):
    def __init__(self, stylesheet):
        QApplication.__init__(self, [])
        self.setStyleSheet(open(stylesheet).read())
