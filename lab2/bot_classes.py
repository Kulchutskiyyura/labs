from abc import ABC, abstractmethod
from random import  randint
from constant import *
import copy
from message import Message
from Player import Player
from Image_factory import *

class Bot(ABC):
    
    def __init__(self):
        pass
    @abstractmethod
    def make_choose(self,player):
        pass
    @abstractmethod
    def change_health_amount(self,number):
        pass
    @abstractmethod
    def _die(self):
        pass
    @abstractmethod
    def __copy__(self):
        pass
    def get_coordinate(self):
         return [self.x_coordinate,self.y_coordinate]
    @abstractmethod
    def get_list_of_choose():
        pass
         
#--------------------------------------------------------/
class Abstract_warriors(Bot):
    @abstractmethod
    def hit(self,player):
        pass
    @abstractmethod
    def defend(self):
        pass
    def __init__(self):
        self.war_mod=False
                  

class Abstract_traders(Bot):
    @abstractmethod
    def buy(self):
        pass
    @abstractmethod
    def sell(self):
        pass
    def __init__(self):
        self.war_mod=False
        self.ready_to_sell=False

class Abstract_monsters(Bot):
    @abstractmethod
    def hit(self,player):
        pass
    @abstractmethod
    def eat(self,player):
        pass

class Abstract_civilian(Bot):
    @abstractmethod
    def ask_for_help(self):
        pass

class Abstract_location(ABC):
     @abstractmethod
     def __init__(self):
         pass
#------------------------------------------------------------------------------------------------------------------------------------------

class Forest_warriors( Abstract_warriors):
   
    
    def __init__(self,health,damage,armor,name,typee):
       super().__init__()
       self.health=health
       self.damage=damage
       self.armor=armor
       self.surrend_price=560
       self.name=name
       self.typee=typee
       self.__list_of_choose_pas=[Message("атакувати",Player.attack)]
       self.__list_of_choose_act=[Message("атакувати",Player.attack),Message("здатися",Player.surrend)]
       self.x_coordinate=None
       self.y_coordinate=None
       self.skin=Image_factory.create_warrior_skin()
    def make_choose(self,player):
       if self.war_mod:
           self.hit(player)

    def get_list_of_choose(self):
        if self.war_mod:
            return self.__list_of_choose_act
        else:
            return self.__list_of_choose_pas

    def change_health_amount(self,number):
        self.health+=number
        self.war_mod=True
    def take_tribute(self,money):
        if money>=self.surrend_price:
            self.war_mod=False
            return True
        return False
    def _die(self):
        pass
    def hit(self,player):
        player.change_health(-self.damage)
    def defend(self):
        pass

    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.armor, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new

class Forest_traders( Abstract_traders):
    
    def __init__(self,health,list_of_goods,name,typee):
        super().__init__()
        self.health= health
        self.list_of_goods=list_of_goods
        self.__list_of_choose_pas=[Message("атакувати",Player.attack),Message("купити",Player.ask_to_show_goods)]
        self.__list_of_choose_act=[Message("атакувати",Player.attack)]
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
        self.skin=Image_factory.create_trader_skin()
    def make_choose(self,player):
       pass
    def change_health_amount(self,number):
        if number<0:
            self.war_mod=True
        self.health+=number
   
    def _die(self):
        pass
   
    def buy(self):
        pass
  
    def sell(self,index,money):
        if money>= self.list_of_goods[index].cost:
            return self.list_of_goods.pop(index)
        else:
            return None

    def get_list_of_choose(self):
        if self.war_mod:
            return  self.__list_of_choose_act
        if self.ready_to_sell:
            return_list=[]
            for i in self.list_of_goods:
                return_list.append(Message(i.name+"  ціна-"+str(i.cost),Player.buy))
            return_list+=self.__list_of_choose_act
            return return_list
        return self.__list_of_choose_pas
    def show_goods(self):
        self.ready_to_sell=True

    def __copy__(self):
        new = self.__class__(self.health, self.list_of_goods ,self.name,self.typee)
        new.__dict__.update(self.__dict__)
        new.list_of_goods = copy.deepcopy(self.list_of_goods)
        return new

class Forest_monsters( Abstract_monsters):
    def __init__(self,health,damage,toxicity,name,typee):
        self.health=health
        self.damage=damage
        self.toxicity=toxicity
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
        self.__list_of_choose=[Message("атакувати",Player.attack)]
        self.skin=Image_factory.create_monster_skin()
    def make_choose(self,player):
        self.hit(player)
    
    def change_health_amount(self,number):
           self.health+=number
   
    def _die(self):
        pass
   
    def hit(self,player):
        player=Player()
        player.change_health(-self.damage)
        number=randint(0,100)
        if number==2:
            self.eat(player)
    def eat(self,player:Player):
        player.change_health(-palyer.health)
    def get_list_of_choose(self):
        return self.__list_of_choose
    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.toxicity, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new

class Forest_civilian( Abstract_civilian):
    def __init__(self,health,name,typee):
        self.health=health
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
        self.__list_of_choose=[Message("атакувати",Player.attack)]
        self.skin=Image_factory.create_civilian_skin()
    def make_choose(self,player):
        pass
    
    def change_health_amount(self,number):
        self.health+=number
   
    def _die(self):
        pass
    def ask_for_help(self):
        pass
    def get_list_of_choose(self):
        return self.__list_of_choose
    def __copy__(self):
        new = self.__class__(self.health, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
class Forest_location(ABC):
    def __init__(self):
       pass

#------------------------------\
class Desert_warriors( Abstract_warriors):
   
    
    def __init__(self,health,damage,armor,name,typee):
       super().__init__()
       self.health=health
       self.damage=damage
       self.armor=armor
       
       self.name=name
       self.typee=typee
       self.x_coordinate=None
       self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
    def _die(self):
        pass
    def hit(self):
        pass
    def defend(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.armor, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
    def get_list_of_choose():
        pass
class Desert_traders( Abstract_traders):
    
   
    def __init__(self,health,list_of_goods,name,typee):
        self.health= health
        self.list_of_goods=list_of_goods
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
   
    def _die(self):
        pass
   
    def buy(self):
        pass
  
    def sell(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health,self.list_of_goods, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        new.list_of_goods = copy.deepcopy(self.list_of_goods)
        return new
    def get_list_of_choose():
        pass
class Desert_monsters( Abstract_monsters):
    def __init__(self,health,damage,toxicity,name,typee):
        self.health=health
        self.damage=damage
        self.toxicity=toxicity
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
   
    def _die(self):
        pass
    def hit(self):
        pass
  
    def eat(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.toxicity, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
    def get_list_of_choose():
        pass
class  Desert_civilian( Abstract_civilian):
    def __init__(self,health,name,typee):
        self.health=health
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
   
    def _die(self):
        pass
    def ask_for_help(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
    def get_list_of_choose():
        pass
class Desert_location( ):
    def __init__(self):
       pass
#-------------------------------------------------------/
class Town_warriors( Abstract_warriors):
   
    
    def __init__(self,health,damage,armor,name,typee):
       super().__init__()
       self.health=health
       self.damage=damage
       self.armor=armor
   
       self.name=name
       self.typee=typee
       self.x_coordinate=None
       self.y_coordinate=None
    def make_choose(self):
        pass
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
    def _die(self):
        pass
    def hit(self):
        pass
    def defend(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.armor, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
    def get_list_of_choose():
        pass
class Town_traders( Abstract_traders):
       
    def __init__(self,health,list_of_goods,name,typee):
        self.health= health
        self.list_of_goods=list_of_goods 
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
   
    def _die(self):
        pass
   
    def buy(self):
        pass
  
    def sell(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health,self.list_of_goods, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        new.list_of_goods = copy.deepcopy(self.list_of_goods)
        return new
    def get_list_of_choose():
        pass
class Town_monsters( Abstract_monsters):
    def __init__(self,health,damage,toxicity,name,typee):
        self.health=health
        self.damage=damage
        self.toxicity=toxicity
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
   
    def _die(self):
        pass
    def hit(self):
        pass
  
    def eat(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.toxicity, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
    def get_list_of_choose():
        pass
class Town_civilian( Abstract_civilian):
    def __init__(self,health,typee,name):
        self.health=health
        self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
    def make_choose(self):
        pass
    
    def change_health_amount(self,number):
        pass
   
    def _die(self):
        pass
    def ask_for_help(self):
        pass
    def __copy__(self):
        new = self.__class__(self.health, self.name,self.typee)
        new.__dict__.update(self.__dict__)
        return new
    def get_list_of_choose():
        pass
class Town_location( ):
    def __init__(self):
       pass
#-------------------------------------------------------/

