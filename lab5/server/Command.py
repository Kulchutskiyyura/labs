from abc import ABC, abstractmethod
class Command(ABC):
    _receiver=None
    @abstractmethod
    def execute(self):
        pass
    @staticmethod
    def set_receiver(receiver):
       print("set_receiver is on")
       Command._receiver=receiver


class Save_command(Command):
    def execute(self):
        Save_command._receiver.save()


class Back_command(Command):
    def execute(self):
         Back_command._receiver.back()


class Choose_command(Command):
    def execute(self,index_of_choose=0):
       Choose_command._receiver.make_choose(user_choose=index_of_choose)

