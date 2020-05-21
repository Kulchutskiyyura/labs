# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore, QtWidgets
from Facade import Facade
from constant import list_of_coordinates
from threading import Lock, Thread
from PySide2.QtCore import *
from PySide2.QtGui import *
lock=True
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.slider = QtWidgets.QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(10)
        self.layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.addOrRemoveButton)
        self.buttons_main = []
        self.buttons_bot = []
        self.user_choose= [0,0]
        self.player = QtWidgets.QTextEdit()
        self.bot = QtWidgets.QTextEdit()
        self.layout.addWidget(self.player)
        self.layout.addWidget(self.bot)
        self.setGeometry(900, 500, 300, 550)
    def addOrRemoveButton(self, value):
        return
        if value > len(self.buttons_main ):
            self.buttons_main.append(QtWidgets.QPushButton("jiji"))
            self.layout.addWidget(self.buttons_main[-1])
        else:
            self.layout.removeWidget(self.buttons_main[-1])  # удаляем из layout-a
            self.buttons_main[-1].setParent(None)  # лишаем родителя
            del self.buttons_main[-1]  # удаляем физически
    def update_screen(self,list_of_choose,user_info,bot_info):
        print("update  ",list_of_choose)

        self.player.clear()
        for i in user_info:

            self.player.insertPlainText(i+"\n")
        self.bot.clear()
        for i in bot_info:

            self.bot.insertPlainText(i+"\n")


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


    def active_main(self):
        lock=True
        button=self.sender()
        value=button.text()

        for i in range(len(self.buttons_main)):
            if self.buttons_main[i].text()==value:
                 self.user_choose=[0,i]
                 print("user_choose:",self.user_choose)
        choose()

    def active_bot(self):
        lock=True
        button=self.sender()
        value=button.text()

        for i in range(len(self.buttons_bot)):
            if self.buttons_bot[i].text()==value:
                self.user_choose=[1,i]
                print("user_choose:",self.user_choose)
        choose()
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

def choose():
    facade=Facade()
    facade.make_choose()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Interface=Facade( Window())
    Interface.start_game(0)
    Interface.make_choose(True)
    sys.exit(app.exec_())

