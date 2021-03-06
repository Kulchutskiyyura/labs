from abc import ABC
from abc import abstractclassmethod
from constant import*
from expresion import Token
from expresion import Interpretator
from expresion import find_index_of_token
from expresion import rfind_index_of_token
from expresion import find_end_of_brackets_index 
from expresion import find_function_argument
from check_function import cheack_if_arguments_is_the_same
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
        self.eror=False
        if local_var_dict.get(self.id)!=None:
            self.local_var=True
        elif var_dict.get(self.id)!=None:
            self.local_var=False
        else:
            self.eror=True
    def next(self):
       
        if self.value==None:
            print("asigment value is none")
            return None
           
        if id==None:
            print("asigment id is none")
            return None
        print("next_as")
        if self.eror==False:
            if self.local_var:
                local_var_dict[self.id]=self.value
            else:
                var_dict[self.id]=self.value
        else:
            pass

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
class Function_statment(Statment):
    def __init__(self, list_of_token):
           self.index=find_index_of_token(list_of_token,END,BREAK)
           self.id=list_of_token[0]._value
           interpretator=Interpretator(list_of_token[0:self.index])
           self.value=interpretator.var_defenition()
           print("self.value(function)", self.value)
           self.list_of_token=list_of_token
    def next(self):
        if self.value==None:
            print("function value is none")
            return None
           
        if id==None:
            print("function id is none")
            return None
        print("function next")
        if self.index+1<len( self.list_of_token):
             return self.index+1
        return None
class Function_definition_statment(Statment):
    def __init__(self, list_of_token):
        #додати перевірку на неоднаковість параметрів
      
        self.id=list_of_token[0]._value
        self.eror=False
        index_of_first_bracket=find_index_of_token(list_of_token,"(",BREAK)
        index_of_second_bracket=find_index_of_token(list_of_token,")",BREAK)
        self.number_of_del_token=2
        del list_of_token[index_of_first_bracket]
        del list_of_token[index_of_second_bracket-1]
        self.index_begin_fun=find_index_of_token(list_of_token,"{",BREAK)
        self.index_end_fun=find_end_of_brackets_index(list_of_token,"{","}")
        self.function_argument=find_function_argument(list_of_token[: self.index_begin_fun])
        if (user_funct_dict.get(self.id)!=None and user_funct_dict[self.id].get(len(self.function_argument))!=None )or funct_dict.get(self.id)!=None:
            self.eror=True
        if cheack_if_arguments_is_the_same(self.function_argument):
            print("function have the same argument(function defenition)")
            self.eror=True
        self.list_of_token=list_of_token
    def next(self):
        if self.eror:
            return 
        if user_funct_dict.get(self.id)==None:
            user_funct_dict[self.id]={}
            #*self.function_argument
        user_funct_dict[self.id][len(self.function_argument)]=[[item[0] for item in self.function_argument],self.list_of_token[self.index_begin_fun+1: self.index_end_fun]]
        print(user_funct_dict)
        if self.index_end_fun+1<len( self.list_of_token):
             return self.index_end_fun+self.number_of_del_token
        return None

class Return_statment(Statment):
    def __init__(self, list_of_token):
        self.index=find_index_of_token(list_of_token,END,BREAK)
        
        self.id=list_of_token[0]._value
        interpretator=Interpretator(list_of_token[1:self.index])
        self.value=interpretator.var_defenition()
        print("self.value(return)", self.value)
        self.list_of_token=list_of_token
        self.eror=False
    def next(self):
       
        if self.value==None:
            print("asigment value is none")
            return None
           
        if id==None:
            print("asigment id is none")
            return None
        print("returnstatment_next_function")
        if self.eror==True:
            pass
        return None

           
        





    




    

   


    
