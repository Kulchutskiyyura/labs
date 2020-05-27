class Message:
    def __init__(self,text,function):
        self.text=text
        self.function=function
    def __repr__(self):
        return self.text
    def __str__(self):
        return self.text
