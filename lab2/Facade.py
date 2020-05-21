from create_coordinate_list import create_coordinate_list
import threading
from map_factory import*
from Game import Game,User_exception
import time
class Facade_meta(type):
    """
    Singelton realisation for Game class
    """
    _instance = None

    def __call__(self,*args,**kwargs) :
        if self._instance is None:
            self._instance = super().__call__(*args,**kwargs)
        return self._instance

class Facade(metaclass=Facade_meta):
    def __init__(self,interface=None):
        self.interface=interface
    def start_game(self,location_type):
        create_coordinate_list(list_of_levels_length[location_type])
        location_dict={}
        if(location_type==0):
            location_dict=self.__create_location(Forest_map_fectory())
        elif location_type==1:
            location_dict=self.__create_location(Desert_map_fectory())
        elif location_type==2:
            location_dict=self.__create_location(Town_map_fectory())
        player=Player(250,1000,[],[copy.copy(Elexir_prototype_factory.warrior_elexir),copy.copy(Elexir_prototype_factory.poison)],[copy.copy(Weapon_prototype_factory.sword)],[0,0])
        self.main_game= Game( location_dict["warrirors_list"],location_dict["traders_list"],location_dict["monssters_list"],location_dict["civilian_list"],location_dict["location"],player,location_type)
        self.main_game.change_cuurent_bot()
        self.interface.show()
        self.user_choose=None

    def __create_location(self,factory: Abstract_map_fectory):
        warrirors_list=factory.create_warriors()
        civilian_list=factory.create_civilian()
        traders_list=factory.create_traders()
        monssters_list=factory.create_monsters()
        location=factory.create_location()
        return {"warrirors_list":warrirors_list,"civilian_list":civilian_list,"traders_list":traders_list,"monssters_list":monssters_list,"location":location}

    def make_choose(self,first_choose=False):
        if not first_choose:
            try:
                self.main_game.perform_user_choose(self.interface.user_choose)
                self.main_game.perform_bot_choose()
            except User_exception as e:
                if e.text=="Game over":
                    self.__game_end()
                    return
        list_of_choose=self.main_game.get_list_of_choose()

        print(list_of_choose)
        self.interface.update_screen(list_of_choose,self.main_game.get_user_info(),self.main_game.get_bot_info())
        #self.__sleep()
        #index=input("зробіть вибір: ")
        #index_1=int(index[0])
        #index_2=int(index[1])



    def __game_end(self):
        self.interface.game_end()
        print("game end")


