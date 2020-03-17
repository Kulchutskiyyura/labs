from Statmen import find_index_of_token
from Statmen import rfind_index_of_token
from Statmen import Interpretator
from Statmen import Asigment
from Statmen import If_statment
from Statmen import While_statment
from Statmen import Function_statment 
from Statmen import Function_definition_statment
from Statmen import Return_statment
from constant import *
from Token import Token
from parser_return import Parser_return
from separator import separator
from linker import linker
 
def parser(list_of_token,local=False):
    
    print('new parser')
    print("list of token in parser",list_of_token)
    token_index=0
    is_loop=False
    can_use_elif=False
    while(1):
        #print("\n\n\n\nlocal var dict in parser ",local_var_dict)
        if list_of_token[token_index]._typee==VAR:
            if list_of_token[token_index+1]._value!=EQ or list_of_token[token_index+1]._typee!=SIGN:
                print("dont have = after varible","variable =" ,list_of_token[token_index]._value)
                print("next token= ",list_of_token[token_index-5:token_index+3])
                return None
            else:
                print("asigment")
                asigment=Asigment(list_of_token[token_index:])
                next=asigment.next()
                if next==None :
                    break
                else:
                    print("next=",next)
                    print("token index",token_index)
                    print("list_of_token",list_of_token)
                    token_index+=next

        elif list_of_token[token_index]._typee==DEFINITION:
             if list_of_token[token_index+2]._value!=EQ or list_of_token[token_index+2]._typee!=SIGN:
                 print("dont have = after varible(parser)","variable =" ,list_of_token[token_index]._value)
                 return None
             if list_of_token[token_index+1]._typee!=VAR:
                 print("dont have varible(parser)")
                 return None
             if local:
                 print("var def")
                 local_var_dict[list_of_token[token_index+1]._value]=Token(list_of_token[token_index+1]._value,VAR)
             else:
                print("var def")
                var_dict[list_of_token[token_index+1]._value]=Token(list_of_token[token_index+1]._value,VAR)
             asigment=Asigment(list_of_token[token_index:],True)
             next=asigment.next()
             if next==None :
                   break
             else:
                   token_index+=next
        elif list_of_token[token_index]._typee==FUN_DEFINITION:
            if  list_of_token[token_index+1]._typee!=FUNCTION:
                 print("dont have fun after fun def (parser)", list_of_token[token_index+1])
                 return None
            print("function def  parser")
            print("curent token list ")
            fun_definition=Function_definition_statment(list_of_token[token_index+1:])
            next=fun_definition.next()
            print("next fun def",next)
            if next==None :
                   break
            else:
                   token_index+=next
                   print("token_index fun def ",token_index)

        elif list_of_token[token_index]._typee==IF:
            if (list_of_token[token_index+1]._value!="(" or list_of_token[token_index+1]._typee!=BREAK) and list_of_token[token_index]._value!=ELSE:
                 print("dont have ( after if (parser)")
                 return None
            else:
                 print("\n\n\nif parser\n\n\n")
                 if_statment= If_statment(list_of_token[token_index:])
                 if ((if_statment.id==ELSE or if_statment.id==ELIF) and not can_use_elif):
                     if_statment.value=Token("0",PATERN)
                     print("\n\n can not use if \n\n\n")
                 next=if_statment.next()
                 if next==None :
                    break
                 else:
                    token_index+=next
                 can_use_elif=if_statment.go_to_elif
        elif list_of_token[token_index]._typee==LOOP:
             if (list_of_token[token_index+1]._value!="(" or list_of_token[token_index+1]._typee!=BREAK) :
                 print("dont have ( after while (parser)")
                 return None
             else:
                 print("\n\n while \n\n\n")
                 while_statment= While_statment(list_of_token[token_index:])
                 next=while_statment.next()
                 if next==None :
                    break
                 elif next==0:
                    print("\n\n next =0 \n\n\n")
                    parser_return=parser(list_of_token[token_index+while_statment.index_begin_while+1:while_statment.index_end_while+token_index])
                    if parser_return==None:
                        token_index+=next
                    elif type(parser_return)==Parser_return:
                        if parser_return.return_type==RETURN:
                            return parser_return
                        elif parser_return.return_type==LOOP_BREAK:
                            token_index+=while_statment.index_end_while
                    else:
                        print("\n\neror with parser return(LOOP parser)\n\n\n")
                 else:
                     token_index+=next
        elif list_of_token[token_index]._typee==FUNCTION:
            if (list_of_token[token_index+1]._value!="(" or list_of_token[token_index+1]._typee!=BREAK) :
                 print("dont have ( after function (parser)")
                 return None
            print("function parser")
            function_statment=Function_statment(list_of_token[token_index:])
            next= function_statment.next()
            if next==None :
                    print("function break")
                    break
            else:
                    print("function")
                    print("next=",next)
                    print("token index",token_index)
                    print("list_of_token",list_of_token)
                    token_index+=next    
        elif list_of_token[token_index]._typee==RETURN:
             if local==False:
                 print("\n\n return in global space \n\n\n")
             return_statment=Return_statment(list_of_token[token_index:])
             print("return parser")
             if return_statment.eror==False:
                 return Parser_return (return_statment.value,RETURN)
        elif list_of_token[token_index]._typee==LOOP_BREAK:
            print("break loop  parser")
            return Parser_return (None,LOOP_BREAK)
        elif list_of_token[token_index]._typee==BREAK:
            print("break parser")
            if token_index+1<len(list_of_token):
                token_index+=1
            else:
                break
        
    print("\n\n\n\n\n parser finish his work, local= ",local,"\n\n\n")
        
                    

