from constant import*
from token import Token
from check_function import cheack_if_number



def run_function(function):
    if function[0]._value not in funct_dict:
        return None
    if function[0]._value=="print":
        return_value=Print(*function[1:])
        return return_value
    elif function[0]._value=="type":
        if len(function[1:])!=funct_dict["type"]:
            print("len argument in type = ",len(function[1:]))
            return None
        print("type function")
        return_value=Type(function[1])
        return return_value
    elif function[0]._value=="int":
        if len(function[1:])!=funct_dict["int"]:
            return None
        return_value=Int(function[1])
        return return_value
    elif function[0]._value=="float":
        if len(function[1:])!=funct_dict["float"]:
            return None
        return_value=Float(function[1])
        return return_value
    elif function[0]._value=="string":
        if len(function[1:])!=funct_dict["string"]:
            return None
        return_value=String(function[1])
        return return_value
    elif function[0]._value=="input":
        if len(function[1:])!=funct_dict["input"]:
            return None
        return_value=Input(function[1])
        return return_value





def Print(*args):
    print("\n\n\n\n\n")
    for i in args:
        print(i._value,end="")
    print("\n\n\n\n\n")
    return Token(str(len(args)),NUMBER)

def Type(argument):
    return Token(argument._typee,STRING)

def Int(argument):
    if cheack_if_number(argument._value)!=-1:
        return Token(str(int(float(argument._value))),NUMBER)
    else:
        return None
def Float (argument):
    if cheack_if_number(argument._value)!=-1:
        return Token(str(float(argument._value)),NUMBER)
    else:
        return None
def String (argument):
    return Token(argument._value,STRING)

def Input(argument):
    return_value=input(argument._value)
    return Token(return_value,STRING)
    