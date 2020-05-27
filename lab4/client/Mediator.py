# This Python file uses the following encoding: utf-8
from PySide2 import QtWidgets
from abc import ABC, abstractmethod
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender,event) -> None:
            pass

class Game_mediator(Mediator):
    def __init__(self,window,button_main_list,buttons_bot_list):
        self.window=window
        self.button_main_list=button_main_list
        self.buttons_bot_list=buttons_bot_list
    def notify(self, sender,event):
        if event=="save":
            self.__save_event()
        elif event=="make_choose_main":
            self.__make_choose_main_event(sender)
        elif event=="make_choose_bot":
            self.__make_choose_bot_event(sender)
        elif event=="back":
            self.__back_event()

    def set_save_command(self,command):
        self.save_command=command

    def set_back_command(self,command):
        self.back_command=command

    def set_choose_command(self,command):
         self.choose_command=command

    def __make_choose_main_event(self,sender):
        value=sender.text()
        user_choose=[]
        for i in range(len(self.button_main_list)):
            if self.button_main_list[i].text()==value:
                 user_choose=[0,i]

        self.choose_command.execute(user_choose)
        if self.choose_command.data=="game_end":
            self.window.game_end()
            return
        self.window.update_screen(*self.choose_command.data)
        print("mediator",id(self.button_main_list))
    def __save_event(self):
        self.save_command.execute()

    def __back_event(self):
        self.back_command.execute()
        self.window. update_screen(*self.back_command.data)

    def __make_choose_bot_event(self,sender):
        value=sender.text()
        user_choose=[]
        for i in range(len(self.buttons_bot_list)):
            if self.buttons_bot_list[i].text()==value:
                 user_choose=[1,i]


        self.choose_command.execute(user_choose)
        if self.choose_command.data=="game_end":
            self.window.game_end()
            return
        self.window.update_screen(*self.choose_command.data)
