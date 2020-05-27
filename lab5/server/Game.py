from constant import *
from User_exception import User_exception
from bot_classes import *
from Caretaker import *


def zero_funct(par):
    pass

class Game():
    def __init__(self,warrirors_list,traders_list,monster_list,civilians_list,location,player:Player,location_type,whant_to_use_elexir=False,whant_to_change_weapon=False,whant_to_change_armor=False,curent_bot=None):
        self.warrirors_list=warrirors_list
        self.traders_list=traders_list
        self.monster_list=monster_list
        self.civilians_list=civilians_list
        self.location=location
        self.player=player
        self.location_type=location_type
        self.whant_to_use_elexir=whant_to_use_elexir
        self.whant_to_change_weapon=whant_to_change_weapon
        self.whant_to_change_armor=whant_to_change_armor
        self.curent_bot=curent_bot

    def get_list_of_choose(self):
        if self.curent_bot:
            print(self.curent_bot.name)

        else:
            print("пусто")
        return_list=[]
        if self.whant_to_use_elexir:
            self.whant_to_use_elexir=False
            list_with_elexir=[]
            for i in range(len(self.player.elexir_list)):
                list_with_elexir.append(Message(self.player.elexir_list[i].name,Game.use_elexir))
            list_with_elexir.append(Message("вийти",zero_funct))
            self.list_of_choose=[list_with_elexir,[]]
        elif  self.whant_to_change_weapon:
             self.whant_to_change_weapon=False
             list_with_weapon=[]
             for i in range(len(self.player.weapon_list)):
                 list_with_weapon.append(Message(self.player.weapon_list[i].name,Game.change_weapon))
             list_with_weapon.append(Message("вийти",zero_funct))
             self.list_of_choose=[list_with_weapon,[]]
        elif self.whant_to_change_armor:
            self.whant_to_change_armor=False
            list_with_armor=[]
            for i in range(len(self.player.armor_list)):
                list_with_armor.append(Message(self.player.armor_list[i].name,Game.change_armor))
            list_with_armor.append(Message("вийти",zero_funct))
            self.list_of_choose=[list_with_armor,[]]
        else:
            self.list_of_choose=[[Message("піти вліво",Game.go_left),Message("піти вправо",Game.go_right), Message("випити еліксир",Game.whant_to_use_elexir),Message("змінити зброю",Game.whant_to_change_weapon),Message("змінити броню",Game.whant_to_change_armor)],self.curent_bot.get_list_of_choose() if self.curent_bot else []]
        for i in range(len(self.list_of_choose)):
            help_list=[]
            for j in range(len(self.list_of_choose[i])):
                help_list.append(str(self.list_of_choose[i][j]))
            return_list.append(help_list)
        return return_list

    def perform_user_choose(self,index):
        if self.player.location[0]>=list_of_levels_length[0]:
            raise User_exception("Game over")
        self.player.answer_id=index[1]
        if index[0]==0:
            self.list_of_choose[index[0]][index[1]].function(self)
        if index[0]==1:
            self.list_of_choose[index[0]][index[1]].function(self.player,self.curent_bot)

    def change_cuurent_bot(self):
        palayer_location=self.player.get_location()
        self.curent_bot=None  
        
        for i in self.warrirors_list+self.traders_list+self.monster_list+self.civilians_list:
            print(i.get_coordinate())
            if i.get_coordinate()==palayer_location:
                self.curent_bot=i
                
                #break
    def go_left(self):
        self.player.location=[self.player.location[0]+1,self.player.location[1]]
        self.change_cuurent_bot()

    def go_right(self):
        self.player.location=[self.player.location[0]+1,self.player.location[1]+1]
        self.change_cuurent_bot()

    def perform_bot_choose(self):
        if self.curent_bot:
            self.curent_bot.make_choose(self.player)
        if self.player.get_health()<=0:
            raise User_exception("Game over")
    def whant_to_use_elexir(self):
        self.whant_to_use_elexir=True
        #index=int(input("enter "))
        #
    def whant_to_change_weapon(self):
        self.whant_to_change_weapon=True

    def whant_to_change_armor(self):
        self.whant_to_change_armor=True

    def get_user_info(self):
        weapon_str=""
        elexir_str=""
        armor_str=""
        for i in self.player.armor_list:
            armor_str+= i.name+" ,"
        for i in self.player.weapon_list:
            weapon_str+= i.name+" ,"
        for i in self.player.elexir_list:
            elexir_str+= i.name+" ,"
        current_weapon_name=""
        if self.player.current_weapon:
            current_weapon_name=self.player.current_weapon.name
        current_armor_name=self.player.current_armor.name
        return ["гравець","здоровя :"+str(self.player.health), "гроші: "+ str(self.player.money),"наявний еліксир: "+elexir_str[:len(elexir_str)-1],"зброя в запасі: "+weapon_str[:len(weapon_str)-1],"вибрана зброя: "+ current_weapon_name, "броня в запасі: "+ armor_str[:len( armor_str)-1],"вибрана броня: "+ current_armor_name]
    def get_bot_info(self):
        if self.curent_bot:
            return [self.curent_bot.name,"здоровя: " + str(self.curent_bot.health)]
        return ["пусто"]
    def use_elexir(self):
        self.player.use_elexir(self.player.answer_id)
    def change_weapon(self):
        self.player.choose_current_weapon(self.player.answer_id)

    def change_armor(self):
        self.player.choose_current_armor(self.player.answer_id)

    def save(self):
        return Game_state_copy(self.__dict__)

    def restore(self, state):
        state_dict=state.get_state()
        for i in state_dict:
            self.__dict__[i]=state_dict[i]
            print(id(self.__dict__[i]), id(state_dict[i]))
        #for i in range(len(self.player.elexir_list)):
 #   print(self.player.elexir_list[i].name," enter",i)
   
"""
       class Game_meta(type):
    
    _instance = None

    def __call__(self,*args,**kwargs) :
        if self._instance is None:
            self._instance = super().__call__(*args,**kwargs)
        return self._instance 
        """

