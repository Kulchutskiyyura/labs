from constant import*
from Token import Token
from check_function import cheack_if_number
import copy 
import parserr
from html_function import find_tag
from html_function import find_tag_with_html
from html_function import get_tag_type
from html_function import get_page
def run_function(function):
    if function[0]._value not in funct_dict and function[0]._value not in user_funct_dict:
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
    elif function[0]._value=="get_page":
        if len(function[1:])!=funct_dict["get_page"]:
            return None
        return_value=get_page(function[1]._value,True)
        if return_value==None:
            return Token("",STRING)
        return return_value
    elif function[0]._value=="find_tag":
        if len(function[1:])!=funct_dict["find_tag"]:
            return None
        return_value=find_tag(function[1]._value,function[2]._value,int(function[3]._value),user_use=True)
        if return_value==None:
            return Token("",STRING)
        return return_value
    elif function[0]._value=="get_tag_type":
        if len(function[1:])!=funct_dict["get_tag_type"]:
            return None
        return_value=get_tag_type(function[1]._value,user_use=True)
        if return_value==None:
            return Token("",STRING)
        return return_value
    elif function[0]._value=="find_tag_with_html":
        if len(function[1:])!=funct_dict["find_tag_with_html"]:
            return None
        return_value=find_tag_with_html(function[1]._value,function[2]._value,int(function[3]._value),user_use=True)
        if return_value==None:
            return Token("",STRING)
        return return_value
    else:

        
       
        if user_funct_dict[function[0]._value].get(len(function[1:])) !=None:
            local_var_dict_copy = copy.deepcopy(local_var_dict) 
            
            local_var_dict.clear()
            print("before argument input function",function[0]._value," local_var_dict= ",local_var_dict)
            print("local_var_dict_copy= ",local_var_dict_copy)
            for i in range(len(function[1:])):
                local_var_dict[user_funct_dict[function[0]._value][len(function[1:])][0][i]._value]=function[1+i]
            print("before parser in user function",function[0]._value," local_var_dict= ",local_var_dict)
            print("global var_dict= ",var_dict)
            return_value=parserr.parser(user_funct_dict[function[0]._value][len(function[1:])][1],local=True)
            print("after parser in user function ",function[0]._value,"local_var_dict= ",local_var_dict)
            print("global var_dict= ",var_dict)
            print(" local_var_dict_copy",local_var_dict_copy)
            local_var_dict.clear()
            local_var_dict.update(local_var_dict_copy)
            print("local var dict after del= ",local_var_dict)
            if return_value==None:
                return_value=Token("0",NUMBER)
            else:
                return_value=return_value.data
            return return_value
        else:
            pass





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
    