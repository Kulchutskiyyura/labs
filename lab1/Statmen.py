from abc import ABC
from abc import abstractclassmethod
from constant import*
from expresion import Token
from expresion import Interpretator
from expresion import find_index_of_token
from expresion import rfind_index_of_token
from expresion import find_end_of_brackets_index 
#from math import a

class Statment(ABC):
    @abstractclassmethod
    def __init__(self,list_of_token):
        pass
    @abstractclassmethod
    def next(self):
        pass



class Asigment(Statment):
    def __init__(self,list_of_token,is_defenition=False):
        #перевірити на помилку
        self.index=find_index_of_token(list_of_token,END,BREAK)
        indentation=2+is_defenition
        self.id=list_of_token[int(is_defenition)]._value
        interpretator=Interpretator(list_of_token[indentation:self.index])
        self.value=interpretator.var_defenition()
        print("self.value(asigment)", self.value)
        self.list_of_token=list_of_token
       
    def next(self):
       
        if self.value==None:
            print("asigment value is none")
            return None
           
        if id==None:
            print("asigment id is none")
            return None
        print("next_as")
        var_dict[self.id]=self.value
        if self.index+1<len( self.list_of_token):
             return self.index+1
        return None

class If_statment(Statment):
    def __init__(self, list_of_token):
        self.id=list_of_token[0]._value
        self.go_to_elif=False
        self.index_begin_if=find_index_of_token(list_of_token,"{",BREAK)
        self.index_end_if=find_end_of_brackets_index(list_of_token,"{","}")
        if (self.id!=ELSE):
            interpretator=Interpretator(list_of_token[1:self.index_begin_if])
            self.value=interpretator.var_defenition()
        else:
             self.value=Token("1",NUMBER) 
        self.list_of_token=list_of_token
        self.exp=0.0000000001
    def next(self):
         if self.value==None:
            print("asigment value is none")
            return None
         if self.value._typee==NUMBER:
             if float(self.value._value)<self.exp:
                 # x * 10 if x < 10 else x / 10
                 if self.index_end_if+1<len(self.list_of_token) and self.list_of_token[self.index_end_if+1]._typee==IF and (self.list_of_token[self.index_end_if+1]._value==ELIF or self.list_of_token[self.index_end_if+1]._value==ELSE):
                     self.go_to_elif=True
                 return self.index_end_if+1 if self.index_end_if+1<len(self.list_of_token) else None
             else:
                  return self.index_begin_if+1 if self.index_begin_if+1<len(self.list_of_token) else None
         elif self.value._typee==STRING:
             if self.value._value=="":
                  if self.index_end_if+1<len(self.list_of_token) and self.list_of_token[self.index_end_if+1]._typee==IF and (self.list_of_token[self.index_end_if+1]._value==ELIF or self.list_of_token[self.index_end_if+1]._value==ELSE):
                      self.go_to_elif=True
                  return self.index_end_if+1 if self.index_end_if+1<len(self.list_of_token) else None
             else:
                 return self.index_begin_if+1 if self.index_begin_if+1<len(self.list_of_token) else None
         elif self.value._typee==PATERN:
              return self.index_end_if+1 if self.index_end_if+1<len(self.list_of_token) else None

class While_statment(Statment):
    def __init__(self, list_of_token):
        self.id=list_of_token[0]._value
        self.index_begin_while=find_index_of_token(list_of_token,"{",BREAK)
        self.index_end_while=find_end_of_brackets_index(list_of_token,"{","}")
        interpretator=Interpretator(list_of_token[1:self.index_begin_while])
        self.value=interpretator.var_defenition()
        self.list_of_token=list_of_token
        self.exp=0.0000000001
    def next(self):
        if self.value==None:
            print("asigment value is none")
            return None
        if self.value._typee==NUMBER:
             if abs(float(self.value._value))<self.exp:
                 # x * 10 if x < 10 else x / 10
                 
                 return self.index_end_while+1 if self.index_end_while+1<len(self.list_of_token) else None
             else:
                  return 0
        elif self.value._typee==STRING:
             if self.value._value=="":
                  
                  return self.index_end_while+1 if self.index_end_while+1<len(self.list_of_token) else None
             else:
                 return 0

    




    

   


    
