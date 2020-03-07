var_dict={}
funct_dict={}
VAR="var"
MUL="*"
DIV="/"
SUB="-"
ADD="+"
END=";"
EQ="="
COMMENT="comment"
NUMBER="number"
STRING="string"
SIGN="sign"
PRINT="print"
BREAK="break"
FUNCTION="function"
PATERN="patern"
IF="if"
#var q=((4+5)*2)+(7-7.2)/5; помилка
class Token():
    def __init__(self,value,typee):
        self._typee=typee
        self._value=value
    def __repr__(self):
        return  f"value :{self._value}  type:{self._typee}"
    def __str__(self):
        return  f"value :{self._value}  type:{self._typee}"
    def __eq__(self, value):
        if (self._value==value._value and self._typee==value._typee):
            return True
        else:
            return False




class Interpretator():
    break_counter=0 
    if_is_true=True
    def __init__(self,text):
        Interpretator.break_counter+=0
        Interpretator.if_is_true

        self.is_defenition=False
        if text[0:len(VAR)]==VAR:
            st=text.replace(" ","")
            if st[len(VAR)]!=EQ:
                self.is_defenition=True
                text=text[len(VAR):]

        self.isprint=False
        if text[0:len(PRINT)]==PRINT:
            self.isprint=True
            text=text[len(PRINT):]
        self.eror=False
        self.text=text.replace(" ","")
        
        self.is_if=False
        if text[0:len(IF)]==IF and text[len(IF)]!="=":
            self.is_if=True
        self.list_of_token=[]
        self.value=None

    def create_token_list(self,string,list_of_token,list_with_pattern,must_be_variable=False):
        #string.isalnum() or self.cheack_if_number(string) or string in list_with_pattern or self.is_string(string)
        print(must_be_variable)
        if len(string)==1:
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
            else:
                try:
                    #print("qqqqqqqqqqqqqqqqqqqqqqqq")
                    if must_be_variable:
                        list_of_token.append(string[0])
                        print("must be var!!!")
                    else:
                        print("must not be var!!!",must_be_variable)
                        token=var_dict[string[0]._value]
                        list_of_token.append(token)

                    
                except KeyError: 
                    print("indefinite varible "+string) 
                    self.eror=True
                finally:
                    return
        if  rfind_index_of_token(string,EQ,SIGN)!=-1:
            print("eq string",string)
            index=rfind_index_of_token(string,EQ,SIGN)  
            list_of_token.append(string[index])
            self.create_token_list(string[0:index],list_of_token,list_with_pattern,True)
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
        

        else:
            return
    def separate_to_substring(self,string,number,list_with_pattern):
        index=find_index_of_token(string,"(",BREAK) #        find("(")
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
            string_new=string[index+1:index_2]
            str_patern="__"+str(number)
            string=string[:index]+[Token(str_patern,PATERN)]+string[index_2+1:]
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
        while len(list_reverse)>1:
            print("begin",len(list_reverse))
            sign=list(filter(lambda x: x._typee==SIGN,list_reverse))[0]
            index=list_reverse.index(sign)
            print(list_reverse[index-1])
            print(list_reverse[index-2])
            print(list_reverse[index])
            if (list_reverse[index-1]._typee==list_reverse[index-2]._typee or list_reverse[index-1]._typee==VAR):
                print("first if")
                if list_reverse[index]._typee==SIGN and list_reverse[index]._value==EQ:
                    print("eq_if",list_reverse[index-1]._value)
                    var_dict[list_reverse[index-1]._value]._typee=list_reverse[index-2]._typee

                    var_dict[list_reverse[index-1]._value]._value=list_reverse[index-2]._value
                    
                    

                    list_reverse[index-2]=Token(list_reverse[index-2]._value , list_reverse[index-2]._typee)
                    del list_reverse[index-1:index+1]
                elif (list_reverse[index-1]._typee==STRING and list_reverse[index]._value==ADD)or  list_reverse[index-1]._typee==NUMBER:
                    print("second if")
                    value=""
                    if list_reverse[index-2]._typee==NUMBER:
                        value=str(eval(list_reverse[index-1]._value+list_reverse[index]._value+list_reverse[index-2]._value))
                    elif list_reverse[index-2]._typee==STRING:
                        value=list_reverse[index-1]._value+list_reverse[index-2]._value
                    list_reverse[index-2]=Token(value,list_reverse[index-1]._typee)
                    del list_reverse[index-1:index+1]
                    print(len(list_reverse),index-2)
                    
                else:
                    print("eror with opetators")
                    return None
                    
            else:
               return None
        print("list rev  ",list_reverse)
        return list_reverse[0]
        
    
    def var_defenition(self):
        if not self.if_is_true:
            if self.text=="{":
                self.break_counter+=1
            elif self.text=="}":
                 self.break_counter+=1
            if self.break_counter==0:
                self.if_is_true=True
                return
            else:
                return
        if self.text in ["{","}"]:
            return
        
        ##print(type(self.text))
        if self.is_if:
            final_list_with_token=self.separate_to_substring(self.text[len(IF):],0,[])
            self.value=self.calculate(final_list_with_token)
            if self.value._value in ["","0"]:
                self.if_is_true=False
            return
        if self.isprint==True:
            if self.cheack_if_number(self.text):
                print(self.text)
            else :
                print("value" ,var_dict[self.text]._value)
            return 

        print("rext var_def",self.text)
        index=self.text.index(EQ)
        
        if var_dict.get(self.text[0:index]):
            try: 
                
                if  self.is_defenition: 
                    raise KeyError () 
                
                   
            except KeyError: 
                    print("redefinition varible "+self.text[0:index]) 
                    return
        else:
             var_dict[self.text[0:index]]=Token(self.text[0:index],VAR)
             try: 
                
                if  not self.is_defenition: 
                    raise KeyError () 
                
                   
             except KeyError: 
                    print("indefined varible "+self.text[0:index]) 
                    return
        #self.create_token_list(self.text[index+1:])
        #self.calculate()
        #final_list_with_token=[]
        list_with_token=linker(self.text)
        print("var_dif , list with token ",list_with_token)
        final_list_with_token=self.separate_to_substring(list_with_token,0,[])
        print("final list rev  ",final_list_with_token)
        self.value=self.calculate(final_list_with_token)
        var_dict[self.text[0:index]]=self.value

def separetor(string,*args,main_sep=";"):
    list_with_string=[]
    is_sub_str=False
    is_coment=False
    last_index=0
    #print(string)
    string=string.replace("\n","")
    #string.replace(" ","")
    print(string)
    for i in range(len(string)):
        if not is_sub_str and not is_coment:
            if string[i] == main_sep:
                if last_index!=i:
                    list_with_string.append(string[last_index:i])
                    last_index=i+1
            elif string[i] in args:
                    if last_index!=i:
                        
                        list_with_string.append(string[last_index:i])
                        list_with_string.append(string[i])
                        last_index=i+1
                    else:
                         list_with_string.append(string[i])
                         last_index=i+1
            elif string[i]=='"':
                is_sub_str=True
            elif string[i]=='<':
                is_coment=True
        else:
            if is_sub_str:
                if string[i]=='"':
                    is_sub_str=False
            if is_coment:
                if string[i]=='>':
                      is_coment=False
    return list_with_string
#i=Interpetator("var b=6+8+a+3")
#i.var_defenition()
def is_string(string):
        if string[0]=='"' :
            st=string[1:]
            st=str(st)
            index=st.find('"')
            if index==len(st)-1:
                return True
            else :
                return False

        else :
            return False
def cheack_if_number(string):
        for i in string:
            if i.isdigit()==False and i!=".":
                break
        else:
            return True
        return False
def is_comment(string):
    if string[0]=="<":
        st=string[1:]
        st=str(st)
        index=st.find('>')
        if index==len(st)-1:
              return True
        else :
              return False

    else :
        return False
def linker(string):
     print("string before separation",string)
     list_with_list=separetor(string+";","*","/","=","-","+","(",")",",",main_sep=";")
     token_list=[]
     print("list after separation ",list_with_list)
     for i in range(len(list_with_list)) :
         if is_string(list_with_list[i]):
             token_list.append(Token(list_with_list[i][1:-1],STRING))
         
         elif cheack_if_number(list_with_list[i]):
             token_list.append(Token(list_with_list[i],NUMBER))
         elif list_with_list[i]  in ["*","/","=","-","+"]:
             token_list.append(Token(list_with_list[i],SIGN))
         elif list_with_list[i] in ["(",")",","]:
             token_list.append(Token(list_with_list[i],BREAK))
         elif list_with_list[i].isalnum():
             if i<len(list_with_list)-1 and     list_with_list[i+1]=="(":
                token_list.append(Token(list_with_list[i],FUNCTION))
             else:
                token_list.append(Token(list_with_list[i],VAR))

     return token_list
def find_index_of_token(token_list,value,type):
    for i in range(len(token_list)):
        if token_list[i]._value==value and token_list[i]._typee==type:
            return i
    return -1
def rfind_index_of_token(token_list,value,type):
    i=len(token_list)-1
    while i>=0:
        if token_list[i]._value==value and token_list[i]._typee==type:
            return i
        i-=1
    return -1
main_program=""
while 1:
    text=input("<input>")
    #list_with_code=text.split("\n")
                  #interpretator=Interpretator(text)
                   #interpretator.var_defenition()
    if text=="run":
        break
    else:
        main_program+=text
    ##print(var_dict)
list_with_program=separetor(main_program,"{","}",main_sep=END)
print("main text" ,main_program)
for i in list_with_program: 
    interpretator=Interpretator(i)
    interpretator.var_defenition()
print(var_dict)


       
    




