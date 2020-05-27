import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore, QtWidgets
from Mediator import *

from threading import Lock, Thread
from PySide2.QtCore import *
from PySide2.QtGui import *
from Command import *

lock=True

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.slider = QtWidgets.QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(10)
        self.layout.addWidget(self.slider)

        self.buttons_main = []
        self.buttons_bot = []
        self.user_choose= [0,0]
        self.player = QtWidgets.QTextEdit()
        self.bot = QtWidgets.QTextEdit()
        self.layout.addWidget(self.player)
        self.layout.addWidget(self.bot)
        self.setGeometry(900, 300, 300, 650)


    def set_mediator(self,mediator):
       self.mediator=mediator


    def update_screen(self,list_of_choose,user_info,bot_info):
        print("update  ",list_of_choose)

        self.player.clear()
        for i in user_info:

            self.player.insertPlainText(i+"\n")
        self.bot.clear()
        for i in bot_info:

            self.bot.insertPlainText(i+"\n")

        print("main",id(self.buttons_main))
        for i in range(len(self.buttons_main)):
            self.layout.removeWidget(self.buttons_main[-1])
            self.buttons_main[-1].setParent(None)
            del self.buttons_main[-1]
        for i in range(len(self.buttons_bot)):
            self.layout.removeWidget(self.buttons_bot[-1])
            self.buttons_bot[-1].setParent(None)
            del self.buttons_bot[-1]
        for i in list_of_choose[0]:
            self.buttons_main.append(QtWidgets.QPushButton(i))
            self.buttons_main[-1].clicked.connect(self.active_main)
            self.layout.addWidget(self.buttons_main[-1])
        for i in list_of_choose[1]:
            self.buttons_bot.append(QtWidgets.QPushButton(i))
            self.buttons_bot[-1].clicked.connect(self.active_bot)
            self.layout.addWidget(self.buttons_bot[-1])

        self.buttons_main.append(QtWidgets.QPushButton("зберегти "))
        self.buttons_main[-1].clicked.connect(self.save)
        self.layout.addWidget(self.buttons_main[-1])

        self.buttons_main.append(QtWidgets.QPushButton(" назад "))
        self.buttons_main[-1].clicked.connect(self.back)
        self.layout.addWidget(self.buttons_main[-1])

    def active_main(self):
        button=self.sender()
        self.mediator.notify(button,"make_choose_main")
    def save(self):
        button=self.sender()
        self.mediator.notify(button,"save")
    def back(self):
        button=self.sender()
        self.mediator.notify(button,"back")
    def active_bot(self):
        button=self.sender()
        self.mediator.notify(button,"make_choose_bot")

    def game_end(self):
         for i in range(len(self.buttons_main)):
             self.layout.removeWidget(self.buttons_main[-1])
             self.buttons_main[-1].setParent(None)
             del self.buttons_main[-1]
         for i in range(len(self.buttons_bot)):
             self.layout.removeWidget(self.buttons_bot[-1])
             self.buttons_bot[-1].setParent(None)
             del self.buttons_bot[-1]
         self.player.clear()
         self.player.insertPlainText("Game end")

    def start_game(self):
        command=Start_command()
        command.execute()
        self.update_screen(*command.data)

if __name__ == '__main__':
    Command.set_host('localhost')
    Command.set_port(9090)
    app = QApplication(sys.argv)
    window_obj=Window()
    mediator=Game_mediator(window_obj,window_obj.buttons_main,window_obj.buttons_bot)
    mediator.set_save_command(Save_command())
    mediator.set_back_command(Back_command())
    mediator.set_choose_command(Choose_command())
    window_obj.set_mediator(mediator)
    window_obj.start_game()
    window_obj.show()

    sys.exit(app.exec_())


"""
def addOrRemoveButton(self, value):
    return
    if value > len(self.buttons_main ):
        self.buttons_main.append(QtWidgets.QPushButton("jiji"))
        self.layout.addWidget(self.buttons_main[-1])
    else:
        self.layout.removeWidget(self.buttons_main[-1])  # удаляем из layout-a
        self.buttons_main[-1].setParent(None)  # лишаем родителя
        del self.buttons_main[-1]  # удаляем физически\
        """

