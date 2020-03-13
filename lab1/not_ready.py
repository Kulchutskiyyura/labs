"""
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




for i in list_with_program: 
    interpretator=Interpretator(i)
    interpretator.var_defenition()





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
       
        self.text=text.replace(" ","")
        
        self.is_if=False
        if text[0:len(IF)]==IF and text[len(IF)]!="=":
            self.is_if=True
        self.list_of_token=[]
        self.value=None




         andd=rfind_index_of_token(string,AND,SIGN)
            eq=rfind_index_of_token(string,EQB,SIGN)
            neq=rfind_index_of_token(string,NEQ,SIGN)
"""