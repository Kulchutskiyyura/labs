from separator import separator
from constant import *
from find_function import*
from check_function import *
from token import Token
def linker(string):
     print("string before separation",string)
     #string=string.replace(" ","")
     print("string after space remove",string)
     list_with_list=separator(string,"*","/","=","-","+","(",")",",",";","{","}","|","&","#","$",">","<","^","!",main_sep="₴")
     token_list=[]
     print("list after separation ",list_with_list)
     for i in range(len(list_with_list)) :
         for_string=list_with_list[i]
         list_with_list[i]=list_with_list[i].replace(" ","")
         if is_string(list_with_list[i]):
             token_list.append(Token(for_string[1:-1],STRING))
         
         elif cheack_if_number(list_with_list[i]):
             token_list.append(Token(list_with_list[i],NUMBER))
         elif list_with_list[i]  in ["*","/","=","-","+","|","&","#","$","<",">","^","!"]:
             if list_with_list[i]=="-":
                 if i-1>0 and list_with_list[i-1] not in ["*","/","=","-","+","|","&","#","$","<",">","^","!"]: #and i+1<len(list_with_list) and list_with_list[i+1] not in ["*","/","=","-","+","|","&","#","$","<",">","^","!"]:
                      token_list.append(Token(list_with_list[i],SIGN))
                 else:
                      token_list.append(Token(SUB_UNAR,SIGN))
             else:
                token_list.append(Token(list_with_list[i],SIGN))
         elif list_with_list[i] in ["(",")",",",";","{","}"]:
             token_list.append(Token(list_with_list[i],BREAK))
         elif list_with_list[i].isalnum():
             if i<len(list_with_list)-1 and     list_with_list[i+1]=="(":
                 #переробити if в один
                if list_with_list[i]==IF:
                    token_list.append(Token(list_with_list[i],IF))
                elif list_with_list[i]==ELIF:
                    token_list.append(Token(list_with_list[i],IF))
                elif list_with_list[i]==WHILE:
                    token_list.append(Token(list_with_list[i],LOOP))
                else:
                    token_list.append(Token(list_with_list[i],FUNCTION))
             else:
                if list_with_list[i]==VAR and list_with_list[i+1]!=EQ:
                     token_list.append(Token(list_with_list[i],DEFINITION))
                elif list_with_list[i]==FUN and list_with_list[i+1]!=EQ:
                     token_list.append(Token(list_with_list[i],FUN_DEFINITION))
                elif list_with_list[i]==ELSE:
                    token_list.append(Token(list_with_list[i],IF))
                else:
                    token_list.append(Token(list_with_list[i],VAR))
    
     return token_list

