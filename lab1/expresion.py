from constant import *
from Token import Token
from linker import linker
from separator import separator
from check_function import *
from find_function import*
from operation import Binary_operators
from operation import Unary_operation
from function import run_function
class Interpretator():
    break_counter=0 
    if_is_true=True
    def __init__(self,token_list):
        Interpretator.break_counter+=0
        Interpretator.if_is_true
        self.token_list=token_list
        self.eror=False
       

    def create_token_list(self,string,list_of_token,list_with_pattern,must_be_variable=False):
        #string.isalnum() or self.cheack_if_number(string) or string in list_with_pattern or self.is_string(string)
        #print(must_be_variable)
        #зробити пріорітети логічним операторам
        #rfind_index_of_token(string,EQB,SIGN)!=-1 or rfind_index_of_token(string,NEQ,SIGN)!=-1 or rfind_index_of_token(string,AND,SIGN)!=-1 or
        if   rfind_index_of_token(string,OR,SIGN)!=-1:
            print("or string",string)
            index=rfind_index_of_token(string,OR,SIGN)    
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif   rfind_index_of_token(string,AND,SIGN)!=-1:
            print("and string",string)
            index=rfind_index_of_token(string,AND,SIGN)    
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif rfind_index_of_token(string,EQB,SIGN)!=-1 or rfind_index_of_token(string,NEQ,SIGN)!=-1:
            index=0
                       ## print("addd")
            eq=rfind_index_of_token(string,EQB,SIGN)
            neq=rfind_index_of_token(string,NEQ,SIGN)
            if eq>neq:
                index=eq
            else :
                index=neq
            list_of_token.append(string[index])
           ## print(index)
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif rfind_index_of_token(string,MORE,SIGN)!=-1 or rfind_index_of_token(string,LESS,SIGN)!=-1:
            index=0
                       ## print("addd")
            more=rfind_index_of_token(string,MORE,SIGN)
            less=rfind_index_of_token(string,LESS,SIGN)
            if more>less:
                index=more
            else :
                index=less
            list_of_token.append(string[index])
           ## print(index) 
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif rfind_index_of_token(string,ADD,SIGN)!=-1 or rfind_index_of_token(string,SUB,SIGN)!=-1:
            index=0
                       ## print("addd")
            add=rfind_index_of_token(string,ADD,SIGN)
            sub=rfind_index_of_token(string,SUB,SIGN)
            if add>sub:
                index=add
            else :
                index=sub
            list_of_token.append(string[index])
           ## print(index)
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif rfind_index_of_token(string,MUL,SIGN)!=-1 or rfind_index_of_token(string,DIV,SIGN)!=-1:
            ##print("mulll")
            index=0
            mul=rfind_index_of_token(string,MUL,SIGN) 
            div=rfind_index_of_token(string,DIV,SIGN)
            if mul>div:
                index=mul
            else :
                index=div
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif   rfind_index_of_token(string,POWER,SIGN)!=-1:
            print("power string",string)
            index=rfind_index_of_token(string,POWER,SIGN)    
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif   rfind_index_of_token(string,NOT,SIGN)!=-1:
            index=rfind_index_of_token(string,NOT,SIGN)    
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        elif   rfind_index_of_token(string,SUB_UNAR,SIGN)!=-1:
            index=rfind_index_of_token(string,SUB_UNAR,SIGN)    
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern)
            self.create_token_list(string[index+1:len(string)],list_of_token,list_with_pattern)
        else:
            if len(string)==1 and string[0]._typee!=SIGN:
                if string[0]._typee==NUMBER or (string[0]._value in list_with_pattern and string[0]._typee==PATERN) :
                    print("token number is",string[0])
                    list_of_token.append(string[0])

                    return
                elif string[0]._typee==COMMENT:
                     return
                elif string[0]._typee==STRING:
                #string=string[1:len(string)-1]
                    print("is string", string)
                
                    list_of_token.append(string[0])
            
                elif string[0]._typee==VAR:
                    try:
                    #print("qqqqqqqqqqqqqqqqqqqqqqqq")
                        if must_be_variable:
                            list_of_token.append(string[0])
                            print("must be var!!!")
                        else:
                            print("must not be var!!!",must_be_variable)
                            token=local_var_dict[string[0]._value]
                            list_of_token.append(token)

                    
                    except KeyError: 
                         
                        try:
                            print("second try")
                           
                            token=var_dict[string[0]._value]
                            print("second try end")
                            list_of_token.append(token)
                           
                        except KeyError:
                            print("indefinite varible "+string)
                            self.eror=True
                    finally:
                        return
                else:
                    return

    def separate_to_substring(self,string,number,list_with_pattern):
        #var x=print(print(4,5,8));
        if string[0]._typee==PATERN and string[0]._value==RUN_FUNCTION:
                string=string[1:]
                function_argument=find_function_argument(string)
                print("function argument ",function_argument)
                list_with_argument_value=[]
                for i in function_argument:
                    
                    argument=self.separate_to_substring(i,0,[])
                    value=self.calculate(argument)
                    list_with_argument_value.append(value)
                print("function argument value  ",list_with_argument_value)
                final_function=create_function_using_functname_and_functargumen(string[0],list_with_argument_value)
                print("final function ",final_function)
                return_value=run_function(final_function)
                return [return_value]
        index=find_index_of_token(string,"(",BREAK) #        find("(")  var x=print((4+5)*2); функція у функції  додавання функцій і чисел+    
        if index==-1:
                token_list=[]
                self.create_token_list(string,token_list,list_with_pattern)
                if not list_with_pattern:
                    value=self.calculate(token_list)
                    token_list=[value]
                print("token_list",token_list)
                return token_list
        else:
            counter=1 
            index_2=index
            for i in range(index+1,len(string)):
                if string[i]._value=="(" and string[i]._typee==BREAK:
                    counter+=1
                if string[i]._value==")" and string[i]._typee==BREAK:
                    counter-=1
                if counter==0:
                    index_2=i
                    break
            else:
                print(string)
                print("problem with ) with index " +str(index+1))
                return 
            str_patern="patern_eror"
            if index-1>=0 and string[index-1]._typee==FUNCTION:
                 string_new=[Token(RUN_FUNCTION,PATERN)]+[string[index-1]]+string[index+1:index_2]
                 str_patern="__"+str(number)
                 string=string[:index-1]+[Token(str_patern,PATERN)]+string[index_2+1:]
            else:
                string_new=string[index+1:index_2]
                str_patern="__"+str(number)
                string=string[:index]+[Token(str_patern,PATERN)]+string[index_2+1:]
            print("list with token after patern",string)
            print("string new",string_new)
            list_with_pattern.append(str_patern)
            number+=1
            print("string -",string)

            list1=self.separate_to_substring(string,number,list_with_pattern)
            list2=self.separate_to_substring(string_new,0,[])
            print("prev",list1,list2)
            index=list1.index(Token(str_patern,PATERN))
            del list1[index]
            print("after del",list1)
            list1=list1[:index]+list2+list1[index:]
            print("return",list1)
            return list1

    
         
       
         
    def calculate(self,list_of_token):
        if self.eror:
            return
        value=0
        print("token_list calcul",list_of_token)
        
        list_reverse=list_of_token[::-1]
        print("list rev  before   ",list_reverse)
        while len(list_reverse)>1:
            
            sign=list(filter(lambda x: x._typee==SIGN,list_reverse))[0]
                 
            index=list_reverse.index(sign)
            if  list_reverse[index]._value in[NOT,SUB_UNAR] :
                 print(list_reverse[index-1])
               
                 print(list_reverse[index])
                 calculation=Unary_operation(list_reverse[index],list_reverse[index-1])
                 value=calculation.eval()
                 list_reverse[index-1]=value
                 del list_reverse[index:index+1]
                 print("unar oper end",list_reverse)
            else:
               
                index=list_reverse.index(sign)
                print(list_reverse[index-1])
                print(list_reverse[index-2])
                print(list_reverse[index])
            #поміняти назву змінної
                calculation=Binary_operators(list_reverse[index],list_reverse[index-1],list_reverse[index-2])
                
                value=calculation.eval()
                list_reverse[index-2]=value
                del list_reverse[index-1:index+1]
                print(len(list_reverse),index-2)
                    
                
        print("list rev  ",list_reverse)
        return list_reverse[0]
        
    
    def var_defenition(self):
        
        

        #print("rext var_def",self.text)
        #index=self.text.index(EQ)
        

        #self.create_token_list(self.text[index+1:])
        #self.calculate()
        #final_list_with_token=[]
        #list_with_token=linker(self.text)
        print("var_dif , list with token ",self.token_list)
        final_list_with_token=self.separate_to_substring(self.token_list,0,[])
        print("final list rev  ",final_list_with_token)
        self.value=self.calculate(final_list_with_token)
        print(self.value)
        return self.value
        #var_dict[self.text[0:index]]=self.value


def create_function_using_functname_and_functargumen(funct_name,argument_list):
    list_of_token_function=[funct_name]
    
    return list_of_token_function+argument_list