import bot_classes

class Weapon:
    def __init__(self,weight,damage,resource,name,cost):
        self.weight=weight
        self.__damage=damage
        self.__resource=resource
        self.cost=cost
        self.__name=name
        self.time_of_life=1
    def hit (self,enemy):
        enemy.change_health_amount(-self.damage)
        self.resource-=20
        if self.resource <= 0:
            self.damage=0
    def set_damage(self,new_damage):
        self.__damage=new_damage
    def get_resource(self):
        return self.__resource
    def set_resource(self,value):
        self.__resource=value
    def get_damage(self):
        return  self.__damage
    def get_name(self):
         return  self.__name
    def set_name(self,new_name):
           self.__name=new_name
    def cheack_if_still_active(self):
        return self
    def __copy__(self):
        new = self.__class__(self.weight, self.damage, self.resource, self.name,self.cost)
        new.__dict__.update(self.__dict__)
        return new
    damage = property(get_damage,set_damage)
    resource= property(get_resource,set_resource)
    name = property(get_name,set_name)

class Weapon_decorator(Weapon):
     _component: Weapon  = None
     def __init__(self, component):
        self._component = component
        self.time_of_life=3
     def component(self) :
        return self._component
     def operation(self):
        return self._component.operation()
     def set_damage(self,new_damage):
        self._component.set_damage(new_damage)
     def hit(self):
         self._component.hit()
     def __copy__(self):
        new = self.__class__(self._component)
        new.__dict__.update(self.__dict__)
        return new
     def get_resource(self):
        return self._component.resource
     def set_resource(self,value):
        self._component.resource=value
     def get_damage(self):
         return  self._component.get_damage()
     def set_damage(self,new_damage):
           self._component.damage=new_damage
     def cheack_if_still_active(self):
        self._component= self._component.cheack_if_still_active()
        if self.time_of_life<=0:
            return self._component
        else:
            return self
     def get_name(self):
         return  self._component.get_name()
     def set_name(self,new_name):
           self._component.name=new_damage
     resource= property(get_resource,set_resource)
     damage = property(get_damage,set_damage)
     name = property(get_name,set_name)

class Monster_elexir_use(Weapon_decorator):
     def hit (self,enemy):
         self.time_of_life-=1
         if isinstance(enemy,bot_classes.Abstract_monsters):
             self._component.set_damage(2*self._component.damage)
             self._component.hit(enemy)
             self._component.set_damage(self._component.damage/2)
         else:
             self._component.hit(enemy)

class Warrior_elexir_use(Weapon_decorator):
     def hit (self,enemy):
         self.time_of_life-=1.5
         print("time_of_life  ", self.time_of_life)
         if isinstance(enemy,bot_classes.Abstract_warriors):
             self._component.set_damage(2*self._component.damage)
             self._component.hit(enemy)
             self._component.set_damage(self._component.damage/2)
         else:
             self._component.hit(enemy)

class Armor_destroy(Weapon_decorator):
     def hit (self,enemy):
        self.time_of_life-=3
        if isinstance(enemy,bot_classes.Abstract_warriors):
            enemy.armor=0
            self._component.hit(enemy)
        else:
            self._component.hit(enemy)

class Poison_use(Weapon_decorator):
    def hit (self,enemy):
        self.time_of_life-=1
        enemy.change_health_amount( self._component.get_damage()*-0.25)
        if isinstance(enemy,bot_classes.Abstract_monsters) or isinstance(enemy,bot_classes.Abstract_warriors):
            enemy.damage=enemy.damage*0.85
        self._component.hit(enemy)
