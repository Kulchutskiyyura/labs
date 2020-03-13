from abc import ABC
from abc import abstractclassmethod
from constant import*
from expresion import Token
from check_function import cheack_if_number
from math import pow
#binary operators
class Operator(ABC):
    @abstractclassmethod
    def eval(self):
        pass
# #-не дорівнює
# ₴-дорівнює
#додати < i >
#перепимати = != для чисел(exp)
class Binary_operators(Operator):
    def __init__(self,operator,exp1,exp2):
        self.operator=operator
        self.exp1=exp1
        self.exp2=exp2
        self.dif=0.0000000001
    def eval(self):
        if self.exp1._typee in [NUMBER,STRING] and self.exp2._typee  in [NUMBER,STRING] and self.operator._typee==SIGN:
               
                if self.exp1._typee==STRING and self.exp2._typee==STRING :
                    if self.operator._value==ADD:
                        return Token(self.exp1._value+self.exp2._value,STRING)
                    elif self.operator._value==AND:
                        return Token(self.exp1._value,STRING) if self.exp1._value!=""and self.exp2._value!="" else Token("",STRING)
                    elif self.operator._value==OR:
                        return Token(self.exp1._value or self.exp2._value,STRING) if self.exp1._value!=""or self.exp2._value!="" else Token("",STRING)
                    elif  self.operator._value==EQB:
                         return Token(self.exp1._value or self.exp2._value or " ",STRING) if self.exp1._value ==self.exp2._value else Token("",STRING)
                    elif  self.operator._value==NEQ:
                         return Token(self.exp1._value or self.exp2._value or " ",STRING) if self.exp1._value !=self.exp2._value else Token("",STRING)
                    elif  self.operator._value==MORE:
                         return Token(" ",STRING) if self.exp1._value > self.exp2._value else Token("",STRING)
                    elif  self.operator._value==LESS:
                         return Token(" ",STRING) if self.exp1._value <self.exp2._value else Token("",STRING)
                    else:
                        print("eror with opetators  (string)")
                        return None
                elif self.exp1._typee==NUMBER and self.exp2._typee==NUMBER:
                    if self.operator._value==ADD:
                        return Token(str(float(self.exp1._value)+float(self.exp2._value)),NUMBER)
                    elif self.operator._value==SUB:
                        return Token(str(float(self.exp1._value)-float(self.exp2._value)),NUMBER)
                    elif self.operator._value==MUL:
                        return Token(str(float(self.exp1._value)*float(self.exp2._value)),NUMBER)
                    elif self.operator._value==DIV:
                        return Token(str(float(self.exp1._value)/float(self.exp2._value)),NUMBER)
                    elif self.operator._value==AND:
                        return Token(self.exp1._value,NUMBER) if self.exp1._value!="0"and self.exp2._value!="0" else Token("0",NUMBER)
                    elif self.operator._value==OR:
                        return Token(str(float(self.exp1._value) or float(self.exp2._value)),NUMBER) if self.exp1._value!="0"or self.exp2._value!="0" else Token("0",NUMBER)
                    elif  self.operator._value==EQB:
                         return Token(str(float(self.exp1._value) or float(self.exp2._value) or "1"),NUMBER) if float(self.exp2._value)-self.dif<float(self.exp1._value) <float(self.exp2._value)+self.dif else Token("0",NUMBER)
                    elif  self.operator._value==NEQ:
                         return Token(str(float(self.exp1._value) or float(self.exp2._value) or "1"),NUMBER) if not(float(self.exp2._value)-self.dif<float(self.exp1._value) <float(self.exp2._value)+self.dif) else Token("0",NUMBER)
                    elif  self.operator._value==MORE:
                         return Token("1",NUMBER) if float(self.exp1._value) >float(self.exp2._value) else Token("0",NUMBER)
                    elif  self.operator._value==LESS:
                         return Token("1",NUMBER) if float(self.exp1._value) < float(self.exp2._value) else Token("0",NUMBER)
                    elif self.operator._value==POWER:
                        #str(float(self.exp1._value)  float(self.exp2._value))
                        return Token(str(pow(float(self.exp1._value),float(self.exp2._value)))  ,NUMBER)
                    else:
                        print("eror with opetators  (number)")
                        return None
                elif self.exp1._typee==STRING and self.exp2._typee==NUMBER:
                     if self.operator._value==MUL:
                         return Token(self.exp1._value*int(self.exp2._value),STRING)
                     elif self.operator._value==AND:
                        return Token(self.exp1._value,STRING) if self.exp1._value!=""and self.exp2._value!="0" else Token("",STRING)
                     elif self.operator._value==OR:
                        return Token(self.exp1._value or self.exp2._value,STRING) if self.exp1._value!=""or self.exp2._value!="0" else Token("",STRING)
                     elif  self.operator._value==EQB:
                         return  Token("",STRING)
                     elif  self.operator._value==NEQ:
                         return Token(" ",STRING) 
                     else:
                        print("eror with opetators  (string\number)")
                        return None
                elif self.exp1._typee==NUMBER and self.exp2._typee==STRING:
                     if self.operator._value==AND:
                        return Token(self.exp1._value,NUMBER) if self.exp1._value!="0"and self.exp2._value!="" else Token("0",NUMBER) 
                     elif self.operator._value==OR:
                        return Token(str(float(self.exp1._value) or (self.exp2._value if cheack_if_number(self.exp2._value) else "1")),NUMBER) if self.exp1._value!="0" or self.exp2._value!="" else Token("0",NUMBER) 
                     elif  self.operator._value==EQB:
                         return  Token("0",NUMBER)
                     elif  self.operator._value==NEQ:
                         return Token("1",NUMBER) 
                     else:
                        print("eror with opetators  (number\string)")
                        return None
                    
        else:
               return None

class Unary_operation(Operator):
     def __init__(self,operator,exp1):
        self.operator=operator
        self.exp1=exp1
        self.dif=0.0000000001
     def eval(self):
         if self.exp1._typee in [NUMBER,STRING] and self.operator._typee==SIGN:
            if(self.exp1._typee==NUMBER):
                if self.operator._value==SUB_UNAR:
                     return Token(str(-float(self.exp1._value)),NUMBER)
                elif self.operator._value==ADD:
                     return Token(str(float(self.exp1._value)),NUMBER)
                elif self.operator._value==NOT :
                    print("operation type=not")
                    return Token("1",NUMBER) if abs(float(self.exp1._value))<self.dif else Token("0",NUMBER)
            elif self.exp1._typee==STRING:
                if self.operator._value==NOT :
                    return Token(" ",STRING) if self.exp1._value=="" else Token("",STRING)
            else:
                return
         else:
            return






"""
           print("second if")
                    value=""
                    if list_reverse[index-2]._typee==NUMBER:
                        value=str(eval(list_reverse[index-1]._value+list_reverse[index]._value+list_reverse[index-2]._value))
                    elif list_reverse[index-2]._typee==STRING:
                        value=list_reverse[index-1]._value+list_reverse[index-2]._value
                    list_reverse[index-2]=Token(value,list_reverse[index-1]._typee)
                    del list_reverse[index-1:index+1]
                    print(len(list_reverse),index-2)
                    """
        
