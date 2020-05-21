from threading import Lock


from Elexir import *

class Player():
      
    def __init__(self,health=None,money=None,armor_list=None,elexir_list=None,weapon_list=None,location=None):
        self.__health=health
        self.money=money
        self.armor_list=armor_list
        self.elexir_list=elexir_list
        self.weapon_list=weapon_list
        self.__location=location
        self.current_weapon=None
        self.answer_id=None
        if self.weapon_list:
            self.choose_current_weapon(0)
        if self.armor_list:
            self.current_armor=self.armor_list[0]
    def use_elexir(self,index):
        if isinstance(self.elexir_list[index],Elexir_for_weapon):
            if self.current_weapon:
                self.current_weapon=self.elexir_list.pop(index).use_elexir(self.current_weapon)

    def attack(self,bot):
        #bot.change_helth_amount(-40)
        if self.current_weapon:
            self._use_weapon(bot)
        else:
            return

    def surrend(self,bot):
        have_enought_money=bot.take_tribute(self.money)
        if not have_enought_money:
            pass
        else:
            self.money-=bot.surrend_price

    def _use_weapon(self,bot):
        self.current_weapon.hit(bot)
        self.current_weapon=self.current_weapon.cheack_if_still_active()
        if self.current_weapon.resource<=0:
            self.current_weapon=None
            if self.weapon_list:
                self.choose_current_weapon(0)

    def choose_current_weapon(self,index):
        if self.current_weapon is not None:
            self.weapon_list.append(self.current_weapon)
        self.current_weapon=self.weapon_list.pop(index)
        
    def choose_current_armor(self,index):
       self.current_armor=self.armor_list.pop(index)
    def get_location(self):
        return self.__location
    def set_location(self,new_location):
        self.__location= new_location
    def get_health(self):
        return self.__health
    def change_health(self,value):
        self.__health+=value
    def buy(self,bot):
        item=bot.sell(self.answer_id,self.money)
        if item!=None:
            self.money-=item.cost
            if isinstance(item,Weapon):
                self.weapon_list.append(item)
            elif isinstance(item,Elexir):
                self.elexir_list.append(item)
        else:
            raise(Exception("нема достатньо грошей:("))

    def ask_to_show_goods(self,bot):
        bot.show_goods()
        print("виберіть товар: ")


    location = property(get_location,set_location)
    health  =  property(get_health,change_health)
    


  


