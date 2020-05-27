from abc import ABC, abstractmethod
from message import Message
from Player import Player
import copy
class Bot_state(ABC):
    @abstractmethod
    def show_trophy(self):
        pass
    @abstractmethod
    def __copy__(self):
        pass
    def set_name(self,name):
        self.name=name
    def __init__(self,list_of_choose_act,list_of_choose_pas):
        self._list_of_choose_act=list_of_choose_act
        self._list_of_choose_pas=list_of_choose_pas
        self.ready_to_show_trophy=False
        self.context=None
    def get_list_of_choose_act(self):
        return self._list_of_choose_act
    def get_list_of_choose_pas(self):
        return self._list_of_choose_pas
    def set_context(self,context):
        #
        self.context=context
        print(type(self.context))
        print("self context list",id(self.context))
        #print("con id",id(self.context.trophy_list))
        #return self.context
    list_of_choose_act=property(get_list_of_choose_act)
    list_of_choose_pas=property(get_list_of_choose_pas)
 
class Alive_bot(Bot_state):
    def __init__(self, list_of_choose_act, list_of_choose_pas):
         super().__init__(list_of_choose_act, list_of_choose_pas)
         self.alive=True
    def show_trophy(self):
        return False
    def __copy__(self):
        new = self.__class__(self._list_of_choose_act, self._list_of_choose_pas)
        new.__dict__.update(self.__dict__)
        new._list_of_choose_act = copy.deepcopy(self._list_of_choose_act)
        new._list_of_choose_pas = copy.deepcopy(self._list_of_choose_pas)
        return new

class Dead_bot(Bot_state):
    def __init__(self, list_of_choose_act, list_of_choose_pas):
         super().__init__(list_of_choose_act, list_of_choose_pas)
         self.alive=False
         self.name="мертвець"
    def show_trophy(self):
        self.ready_to_show_trophy=True
        return False
    def get_list_of_choose_act(self):
            print("current context type",type(self.context))

            return_list=[]
            for i in self.context:
                return_list.append(Message(i.name+"  ",Player.get_trophy))
            return_list+=self._list_of_choose_act
            return return_list
    def get_list_of_choose_pas(self):
        return self._list_of_choose_pas
    def __copy__(self):
        new = self.__class__(self._list_of_choose_act, self._list_of_choose_pas)
        new.__dict__.update(self.__dict__)
        new._list_of_choose_act = copy.deepcopy(self._list_of_choose_act)
        new._list_of_choose_pas = copy.deepcopy(self._list_of_choose_pas)
        return new
    list_of_choose_act=property(get_list_of_choose_act)
    list_of_choose_pas=property(get_list_of_choose_pas)
   
    
