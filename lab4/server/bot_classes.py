from abc import ABC, abstractmethod
from random import  randint
from constant import *
import copy
from Image_factory import *
from state_factory import *
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
    @abstractmethod
    def show_trophy():
        pass
    @abstractmethod
    def give_trophy():
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
   
    
    def __init__(self,health,damage,armor,name,typee,state,trophy_list):
       super().__init__()
       self.trophy_list=trophy_list
       self.state=state
       
       self.state.set_name(name)
       self.health=health
       self.damage=damage
       self.armor=armor
       self.surrend_price=560

       self.state.set_name(name)
       #self.name=name
       self.typee=typee
       #self.__list_of_choose_pas=[Message("атакувати",Player.attack)]
       #self.__list_of_choose_act=[Message("атакувати",Player.attack),Message("здатися",Player.surrend)]
       self.x_coordinate=None
       self.y_coordinate=None
       self.skin=Image_factory.create_warrior_skin()
       #self.state.set_context(self)
    def make_choose(self,player): 
       if self.war_mod and self.state.alive:
           self.hit(player)

    def get_list_of_choose(self):
        if self.war_mod and self.state.alive:
            return self.state.list_of_choose_act
        elif self.state.ready_to_show_trophy:
            return self.state.list_of_choose_act
        else:
            return self.state.list_of_choose_pas


    def change_health_amount(self,number):
        self.health+=number
        self.war_mod=True
        if self.health<=0:
            self._die()
            self.health=0
    def take_tribute(self,money):
        if money>=self.surrend_price:
            self.war_mod=False
            return True
        return False
    def _die(self):
        self.state=copy.copy( State_factory.dead_bot)
        self.state.set_context(self.trophy_list)
        
    def hit(self,player):
        player.take_a_punch(self.damage)
    def defend(self):
        pass

    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.armor, self.name,self.typee,self.state,self.trophy_list)
        new.trophy_list = copy.deepcopy(self.trophy_list)
        new.__dict__.update(self.__dict__)
        new.state.set_context(new.trophy_list)
        return new

    def show_trophy(self):
        self.state.show_trophy()
    def give_trophy(self,index):
        return self.trophy_list.pop(index)
    def get_name(self):
        return self.state.name
    name=property(get_name)

class Forest_traders( Abstract_traders):
     
    def __init__(self,health,list_of_goods,name,typee,state,trophy_list):
        super().__init__()
        self.health= health
        self.trophy_list=trophy_list
        self.list_of_goods=list_of_goods
        #self.__list_of_choose_pas=[Message("атакувати",Player.attack),Message("купити",Player.ask_to_show_goods)]
        #self.__list_of_choose_act=[Message("атакувати",Player.attack)]

        self.state=state
        
        self.state.set_name(name)
        #self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
        self.skin=Image_factory.create_trader_skin()
        #self.state.set_context(self)
    def make_choose(self,player):
       pass
    def change_health_amount(self,number):
        if number<0:
            self.war_mod=True
        self.health+=number
        if self.health<=0:
            self._die()
            self.health=0
    def _die(self):
        self.state=copy.copy( State_factory.dead_bot)
        print("id list die",id(self.trophy_list))
        self.state.set_context(self.trophy_list)
        #print("id die list",id(copy.deepcopy(self.trophy_list)))
    def buy(self):
        pass
  
    def sell(self,index,money):
        if money>= self.list_of_goods[index].cost:
            return self.list_of_goods.pop(index)
        else:
            return None

    def get_list_of_choose(self):
        if self.war_mod and self.state.alive :
            return self.state.list_of_choose_act
        if self.state.ready_to_show_trophy:
            return self.state.list_of_choose_act
        if self.ready_to_sell and self.state.alive:
            return_list=[]
            for i in self.list_of_goods:
                return_list.append(Message(i.name+"  ціна-"+str(i.cost),Player.buy))
            return_list+=self.state.list_of_choose_act
            return return_list
        return self.state.list_of_choose_pas
    def show_goods(self):
        self.ready_to_sell=True

    def __copy__(self):
        new = self.__class__(self.health, self.list_of_goods ,self.name,self.typee,self.state,self.trophy_list)
        new.__dict__.update(self.__dict__)
        new.list_of_goods = copy.deepcopy(self.list_of_goods)
        
        new.trophy_list = copy.deepcopy(self.trophy_list)
        #print("old id good ", id(self.list_of_goods),"new",id(new.list_of_goods))
        #print("old id",id(self.trophy_list),"new",id(new.tropy_list))
        new.state.set_context(new.trophy_list)
        
        return new
    def get_name(self):
        return self.state.name
    def give_trophy(self,index):
       return self.trophy_list.pop(index)
    def show_trophy(self):
        self.state.show_trophy()
    name=property(get_name)

class Forest_monsters( Abstract_monsters):
    def __init__(self,health,damage,toxicity,name,typee,state,trophy_list):
        self.state=state
        

        self.state.set_name(name)
        self.trophy_list=trophy_list
        self.health=health
        self.damage=damage
        self.toxicity=toxicity
        #self.name=name
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
        #self.__list_of_choose=[Message("атакувати",Player.attack)]
        self.skin=Image_factory.create_monster_skin()
        #self.state.set_context(self)
    def make_choose(self,player):
        if self.state.alive:
            self.hit(player)
    
    def change_health_amount(self,number):
           self.health+=number
           if self.health<=0:
            self._die()
            self.health=0
    def _die(self):
       self.state=copy.copy( State_factory.dead_bot)
       self.state.set_context(self.trophy_list)
    def hit(self,player):
        player.take_a_punch(self.damage)
        number=randint(0,20)
        if number==2:
            self.eat(player)
    def eat(self,player):
        player.take_a_punch(player.health)
    def get_list_of_choose(self):
        if self.state.ready_to_show_trophy:
            return self.state.list_of_choose_act
        else:
            return self.state.list_of_choose_pas
    def __copy__(self):
        new = self.__class__(self.health, self.damage, self.toxicity, self.name,self.typee,self.state,self.trophy_list)
        new.trophy_list = copy.deepcopy(self.trophy_list)
        new.__dict__.update(self.__dict__)
        new.state.set_context(new.trophy_list)
        return new
    def get_name(self):
        return self.state.name
    def give_trophy(self,index):
         return self.trophy_list.pop(index)
    def show_trophy(self):
        self.state.show_trophy()
    name=property(get_name)

class Forest_civilian( Abstract_civilian):
    def __init__(self,health,name,typee,state,trophy_list):
        self.state=state
        
        self.state.set_name(name)
        self.trophy_list=trophy_list
        self.health=health
        #self.name=name
        
        self.typee=typee
        self.x_coordinate=None
        self.y_coordinate=None
        #self.__list_of_choose=[Message("атакувати",Player.attack)]
        self.skin=Image_factory.create_civilian_skin()
        #self.state.set_context(self)
    def make_choose(self,player):
        pass
    
    def change_health_amount(self,number):
        self.health+=number
        if self.health<=0:
            self._die()
            self.health=0
    def _die(self):
        self.state=copy.copy( State_factory.dead_bot)
        self.state.set_context(self.trophy_list)
    def ask_for_help(self):
        pass
    def get_list_of_choose(self):
        if self.state.ready_to_show_trophy:
            return self.state.list_of_choose_act
        else:
            return self.state.list_of_choose_pas
    def __copy__(self):
        new = self.__class__(self.health, self.name,self.typee,self.state,self.trophy_list)
        new.trophy_list = copy.deepcopy(self.trophy_list)
        new.__dict__.update(self.__dict__) 
        new.state.set_context(new.trophy_list)
        return new
    def show_trophy(self):
        self.state.show_trophy()
    def get_name(self):
        return self.state.name
    def give_trophy(self,index):
        return self.trophy_list.pop(index)
    name=property(get_name)
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

"""
 if self.war_mod:
            return self.state.__list_of_choose_act
        else:
            return self.state.__list_of_choose_pas




            return_list=[]
            for i in self.list_of_goods:
                return_list.append(Message(i.name+"  ціна-"+str(i.cost),Player.buy))
            return_list+=self.__list_of_choose_act
            return return_list

            """