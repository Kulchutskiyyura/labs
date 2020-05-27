from enum import Enum
class Type_of_locatio(Enum):
    forest=0
    desert=1
    city=2
class Bot_type(Enum):
    ordinary = 1
    elite = 2
    super = 3
class Bot_type(Enum):
    Warrior=1
    Trader=2
    Monster=3
    Civilian=4

list_of_coordinates=[]
list_of_levels_length=[5,8,12]
forest_warriors_min_health=85
forest_warriors_max_health=125
desert_warriors_min_health=65
desert_warriors_max_health=95
town_warriors_min_health=150
town_warriors_max_health=220

forest_traders_min_health=45
forest_traders_max_health=55
desert_traders_min_health=25
desert_traders_max_health=35
town_traders_min_health=45
town_traders_max_health=60

forest_monsters_min_health=180
forest_monsters_max_health=220
desert_monsters_min_health=100
desert_monsters_max_health=120
town_monsters_min_health=75
town_monsters_max_health=85

forest_civilian_min_lhealth=45
forest_civilian_max_health=55
desert_civilian_min_health=25
desert_civilian_max_health=35
town_civilian_min_health=45
town_civilian_max_health=60
