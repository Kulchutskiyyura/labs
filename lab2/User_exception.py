# This Python file uses the following encoding: utf-8


class User_exception(Exception):
    def __init__(self,eror_text):
        self.text=eror_text

    def __str__(self):
        return repr(self.text)
