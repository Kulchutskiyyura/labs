from abc import ABC, abstractmethod
from weapon import*
class Elexir(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def use_elexir():
        pass
    @abstractmethod
    def __copy__(self):
        pass



class Elexir_for_weapon(Elexir):
    def __init__(self,class_type,name,cost):
        self.class_type=class_type
        self.name=name
        self.cost=cost
    def use_elexir(self,weapon):
        return self.class_type(weapon)
    def __copy__(self):
        new = self.__class__(self.class_type, self.name,self.cost)
        new.__dict__.update(self.__dict__)
        return new


