from abc import ABC, abstractmethod
from typing import List
from bot_classes import *
import copy
from random import  randint
from prototype_factory import *
class Abstract_map_fectory(ABC):
    @abstractmethod 
    def create_warriors(self):
        pass
    @abstractmethod
    def create_traders(self):
        pass
    @abstractmethod
    def create_monsters(self):
        pass
    @abstractmethod
    def create_civilian(self):
        pass
    @abstractmethod
    def create_location(self):
        pass
    #Desert

class Forest_map_fectory(Abstract_map_fectory):
    def create_warriors(self):
        forest_warriors_list=[]
        prototype=Forest_prototype_factory.warrior


        for i in range(6):
            warrior= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            warrior.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            warrior.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_warriors_list.append(warrior)
        prototype=Forest_prototype_factory.elite_warrior
        for i in range(2):
            warrior= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            warrior.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            warrior.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_warriors_list.append(warrior)
        return forest_warriors_list 
        
    def create_traders(self):
        forest_traders_list=[]
        prototype= Forest_prototype_factory.trader
        for i in range(8):
            trader= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            trader.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            trader.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_traders_list.append(trader)
        prototype= Forest_prototype_factory.elite_trader
        for i in range(2):
            trader= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            trader.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            trader.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_traders_list.append(trader)
        return forest_traders_list

    def create_monsters(self):
        forest_monsters_list=[]
        prototype= Forest_prototype_factory.monster
        for i in range(5):
            monster= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            
            monster.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            monster.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_monsters_list.append(monster)
        prototype= Forest_prototype_factory.elite_monster
        for i in range(2):
            monster= copy.copy(prototype)

            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            monster.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            monster.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_monsters_list.append(monster)
        return forest_monsters_list

    def create_civilian(self):
        forest_civilian_list=[]
        prototype= Forest_prototype_factory.civilian
        for i in range(3):
            civilian= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            civilian.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            civilian.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            forest_civilian_list.append(civilian)
        return forest_civilian_list
    def create_location(self)->Forest_location:
        return Forest_location()

class Desert_map_fectory(Abstract_map_fectory):
    def create_warriors(self):
        desert_warriors_list=[]
        #print(list_of_coordinates)
        prototype= Desert_prototype_factory.monster
        for i in range(5):
            warrior= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            warrior.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            warrior.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_warriors_list.append(warrior)
        prototype= Desert_prototype_factory.elite_monster
        for i in range(2):
            warrior= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            warrior.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            warrior.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_warriors_list.append(warrior)
        return desert_warriors_list

    def create_traders(self):
        desert_traders_list=[]
        #print(list_of_coordinates)
        prototype= Desert_prototype_factory.trader
        for i in range(1):
            trader= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            trader.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            trader.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_traders_list.append(trader)
        prototype= Desert_prototype_factory.elite_trader
        for i in range(2):
            trader= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            trader.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            trader.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_traders_list.append(trader)
        return desert_traders_list

    def create_monsters(self):
        desert_monsters_list=[]
        prototype=Desert_prototype_factory.monster
        for i in range(1):
            monster= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            monster.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            monster.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_monsters_list.append(monster)
        prototype=Town_prototype_factory.elite_monster
        for i in range(2):
            monster= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            monster.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            monster.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_monsters_list.append(monster)
        return  desert_monsters_list

    def create_civilian(self):
        desert_civilian_list=[]
        prototype= Desert_prototype_factory.civilian
        for i in range(2):
            civilian= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates)-1)
            civilian.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            civilian.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            desert_civilian_list.append(civilian)
        return desert_civilian_list
    def create_location(self)->Desert_location:
        return Desert_location()

    #Town
class Town_map_fectory(Abstract_map_fectory):
    def create_warriors(self):
        town_warriors_list=[]
        prototype= Town_prototype_factory.warrior
        for i in range(2):
            warrior= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            warrior.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            warrior.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            town_warriors_list.append(warrior)
        prototype= Town_prototype_factory.warrior
        for i in range(2):
            warrior= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            warrior.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            warrior.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            town_warriors_list.append(warrior)
        return town_warriors_list
    def create_traders(self):
        town_traders_list=[]
        prototype=Town_prototype_factory.trader
        for i in range(4):
            trader= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            trader.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            trader.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            town_traders_list.append(trader)
        prototype=Town_prototype_factory.elite_trader
        for i in range(2):
            trader= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            trader.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            trader.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            town_traders_list.append(trader)
        return  town_traders_list
    def create_monsters(self):
        town_monsters_list=[]
        prototype=Town_prototype_factory.monster
        for i in range(1):
            monster= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            monster.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            monster.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            town_monsters_list.append(monster)
        prototype=Town_prototype_factory.elite_monster
        for i in range(2):
            monster= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            monster.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            monster.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list]
            town_monsters_list.append(monster)
        return  town_monsters_list
    def create_civilian(self):
        town_civilian_list=[]
        prototype=Town_prototype_factory.civilian
        for i in range(4):
            civilian= copy.copy(prototype)
            index_in_coordinate_list=randint(0,len(list_of_coordinates))
            civilian.x_coordinate=list_of_coordinates[index_in_coordinate_list][0]
            civilian.y_coordinate=list_of_coordinates[index_in_coordinate_list][1]
            del list_of_coordinates[index_in_coordinate_list] 
            town_civilian_list.append(civilian)
        return town_civilian_list
    def create_location(self)->Town_location:
        return Town_location()
