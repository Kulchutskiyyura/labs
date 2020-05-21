from bot_classes import *
from weapon import *
from Elexir import *
class Weapon_prototype_factory:
       sword=Weapon(20,45,100,"меч",250)
       super_sword=Weapon(20,55,100,"дворучний меч",400)
       saber=Weapon(10,50,150,"шабля",350)
       dark_of_night=Weapon(20,80,120,"dark_of_night",1000)
       lance=Weapon(15,60,115,"спис",300)
       escalibur=Weapon(25,120,140,"ескалібур",2000)

class Elexir_prototype_factory:
        monster_elexir=Elexir_for_weapon(Monster_elexir_use,"вбивця монстрів",300)
        armor_elexir=Elexir_for_weapon(Armor_destroy,"руйнівник броні",400)
        poison=Elexir_for_weapon(Poison_use,"отрута ",500)
        warrior_elexir=Elexir_for_weapon(Warrior_elexir_use,"вбивця воїнів",300)
        
class Forest_prototype_factory:
       warrior= Forest_warriors(100,40,15,"воїн","normal")
       elite_warrior= Forest_warriors(125,47,45,"елітний воїн","elit")
       trader= Forest_traders(65,[copy.copy(Weapon_prototype_factory.sword), copy.copy(Weapon_prototype_factory.saber) ,copy.copy(Weapon_prototype_factory.super_sword) ],"торговець","normal")
       elite_trader= Forest_traders(70,[copy.copy(Weapon_prototype_factory.saber) ,copy.copy(Weapon_prototype_factory.super_sword) ,copy.copy(Weapon_prototype_factory.escalibur)],"багатий торговець","elite")
       monster= Forest_monsters(150,50,20,"монстр","normal")
       elite_monster= Forest_monsters(180,57,25,"гігантський монстр","elite")
       civilian= Forest_civilian(50,"мирний житель","normal")

class Desert_prototype_factory:
       warrior= Desert_warriors(100,40,15,"воїн","normal")
       elite_warrior= Desert_warriors(125,47,45,"елітний воїн","elit")
       trader= Desert_traders(65,[],"tarder","normal")
       elite_trader= Desert_traders(70,[],"tarder","elite")
       monster= Desert_monsters(150,50,20,"monster","normal")
       elite_monster= Desert_monsters(180,57,25,"monster","elite")
       civilian= Desert_civilian(50,"civilian","normal")

class Town_prototype_factory:
        warrior= Town_warriors(100,40,15,"warior","normal")
        elite_warrior= Town_warriors(125,47,45,"warior","elit")
        trader= Town_traders(65,[],"tarder","normal")
        elite_trader= Town_traders(70,[],"tarder","elite")
        monster= Town_monsters(150,50,20,"monster","normal")
        elite_monster= Town_monsters(180,57,25,"monster","elite")
        civilian= Town_civilian(50,"civilian","normal")

