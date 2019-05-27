#from PyQt5.QtWidgets import QLabel, QLineEdit
#from magic8ballapp import Magic8BallApp
import random
import json

class Magic8BallEvents:
    def __init__(self, responsefile, message, question, app):
        self.responses = json.loads(open(responsefile).read())
        self.message = message
        self.question = question
        self.app = app

    def ask_button_clicked(self):
        self.message.setText(random.choice(self.responses))

    def clear_button_clicked(self):
        self.question.setText('')

    def play_again_button_clicked(self):
        self.message.setText("What do you want to know?")
        self.question.setText('')

    def quit_button_clicked(self):
        self.app.exit()
