from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QLabel,
    QLineEdit, QPushButton)
from magic8ballapp import Magic8BallApp
from magic8ballevents import Magic8BallEvents

stylesheet = "./css/styles.css"

responsefile = './json/responses.json'

if __name__ == '__main__':
    app = Magic8BallApp(stylesheet)
    window = QWidget()

    layout1 = QVBoxLayout()

    label = QLabel("What do you want to know?")
    layout1.addWidget(label)

    lineedit = QLineEdit('')
    layout1.addWidget(lineedit)

    layout2 = QHBoxLayout()
    layout1.addLayout(layout2)

    events = Magic8BallEvents(responsefile, label, lineedit, app)

    ask_button = QPushButton('Ask')
    layout2.addWidget(ask_button)
    ask_button.clicked.connect(events.ask_button_clicked)

    clear_button = QPushButton('Clear')
    layout2.addWidget(clear_button)
    clear_button.clicked.connect(events.clear_button_clicked)

    play_again_button = QPushButton('Play Again')
    layout2.addWidget(play_again_button)
    play_again_button.clicked.connect(events.play_again_button_clicked)

    quit_button = QPushButton('Quit')
    layout2.addWidget(quit_button)
    quit_button.clicked.connect(events.quit_button_clicked)

    window.setLayout(layout1)
    window.show()
    app.exec_()
