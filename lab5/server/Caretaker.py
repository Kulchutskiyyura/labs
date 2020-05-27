# This Python file uses the following encoding: utf-8
from State_copy import *
class Caretaker:
    def __init__(self,originator):
        self.list_of_state=[]
        self.originator=originator
    def undo(self):
        if not len(self.list_of_state):
            return

        state = self.list_of_state.pop()
        self.originator.restore(state)

    def save_changes(self):
        self.list_of_state.append(self.originator.save())
