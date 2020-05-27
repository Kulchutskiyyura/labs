from bot_state import *

class State_factory:
    alive_warrior =Alive_bot([Message("атакувати",Player.attack),Message("здатися",Player.surrend)],[Message("атакувати",Player.attack)],)
    alive_trader= Alive_bot([Message("атакувати",Player.attack)],[Message("атакувати",Player.attack),Message("купити",Player.ask_to_show_goods)])
    alive_monster= Alive_bot([],[Message("атакувати",Player.attack)])
    alive_civilian= Alive_bot([],[Message("атакувати",Player.attack)])
    dead_bot=Dead_bot([],[Message("взяти трофеї",Player.ask_to_show_trophy)])