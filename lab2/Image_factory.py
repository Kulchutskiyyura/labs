# This Python file uses the following encoding: utf-8
from Skin import Skin
from constant import Bot_type
class Image_factory:
    _Image_dict={}

    @staticmethod
    def create_warrior_skin():
        if not Image_factory._Image_dict.get(Bot_type.Warrior):
            Image_factory._Image_dict[Bot_type.Warrior]=Skin("D:\dudle_jm_img\monster3.png","warrior")
        return Image_factory._Image_dict[Bot_type.Warrior]
    @staticmethod
    def create_trader_skin():
        if not Image_factory._Image_dict.get(Bot_type.Trader):
            Image_factory._Image_dict[Bot_type.Trader]=Skin("D:\dudle_jm_img\monster3.png","trader")
        return Image_factory._Image_dict[Bot_type.Trader]

    @staticmethod
    def create_civilian_skin():
        if not Image_factory._Image_dict.get(Bot_type.Civilian):
            Image_factory._Image_dict[Bot_type.Civilian]=Skin("D:\dudle_jm_img\monster3.png","civilian")
        return Image_factory._Image_dict[Bot_type.Civilian]

    @staticmethod
    def create_monster_skin():
        if not Image_factory._Image_dict.get(Bot_type.Monster):
            Image_factory._Image_dict[Bot_type.Monster]=Skin("D:\dudle_jm_img\monster3.png","monster")
        return Image_factory._Image_dict[Bot_type.Monster]
