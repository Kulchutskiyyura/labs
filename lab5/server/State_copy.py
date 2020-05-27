# This Python file uses the following encoding: utf-8
from abc import ABC, abstractmethod
import copy
import pickle
class State_copy(ABC):
   @abstractmethod
   def get_state(self):
       pass

class Game_state_copy(State_copy):
    number_of_copy=0
    def __init__(self,dict_with_variable):
        Game_state_copy.number_of_copy+=1
        self.id=Game_state_copy.number_of_copy
        self.file_path="D:\lab4semester\game_maps_part_2\game_maps_2_server\PythonApplication1\copy_files\save_state_"+str(self.id)+".pkl"
        pickle.dump(dict_with_variable, open(self.file_path, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    def get_state(self):
        state=pickle.load(open(self.file_path,"rb"))
        return state

