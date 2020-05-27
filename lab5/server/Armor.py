from abc import ABC, abstractmethod
import math

class Armor:
    def __init__(self,strategy):
        self.__strategy=strategy
        if self.__strategy:
            self.name=strategy.name
    def deffend(self,damage):

        damage=self.__strategy.protect(damage)
        return damage
    def set_strategy(self,strategy):
        self.__strategy=strategy
        self.name=strategy.name
    def get_strategy(self):
        return self.__strategy
    strategy= property(get_strategy,set_strategy)

class Armor_type(ABC):
    @abstractmethod
    def protect(self,damage):
        pass
class Heavy_armor(Armor_type):
    def __init__(self):
        self.resource=100
        self.cost=300
        self.name="тяжка броня"
    def protect(self,damage):
        if damage>100:
            damage=damage/2
        else:
            damage=damage/2.2
        return damage
class Light_armor(Armor_type):
    def __init__(self):
        self.resource=100
        self.cost=200
        self.name="легка броня"
    def protect(self,damage):
        if damage>100:
            pass
        elif damage>50:
            damage=damage/1.2
        else:
            damage=damage/1.8
        return damage
class Heal_armor(Armor_type):
    def __init__(self):
        self.resource=100
        self.name="зціляюча броня"
        self.cost=400
    def protect(self,damage):
        damage=damage-40
        return damage
class Super_armor(Armor_type):
    def __init__(self):
        self.resource=100
        self.name="супер броня"
        self.cost=900
    def protect(self,damage):
        if damage<60:
            damage=0
        else:
            damage=damage/5
        damage=damage-25
        return damage
class No_armor(Armor_type):
    def __init__(self):
        self.resource=math.inf
        self.name="жодної броні"
        self.cost=0
    def protect(self,damage):
        return damage
