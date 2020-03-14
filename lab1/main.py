from parserr import parser
from constant import *
from parserr import linker
#var q=((4+5)*2)+(7-7.2)/5; помилка
#i=Interpetator("var b=6+8+a+3") 
#i.var_defenition()
main_program=""             
while 1:
    text=input("<input>")
    #list_with_code=text.split("\n")
                  #interpretator=Interpretator(text)
                   #interpretator.var_defenition()
    if text=="run":
        break
    else:
         if text[0:len(VAR)]==VAR:
            st=text.replace(" ","")
            if st[len(VAR)]!=EQ:
                text=text[0:len(VAR)]+"₴"+   text[len(VAR):]
         main_program+=text
    ##print(var_dict)
#list_with_program=separetor(main_program,"{","}",)
# var₴ x=4;var₴ y=5;var₴ m=0;while(x){if(x$3){m=m+10;}y=5;while(y){if(y$2){m=m+3;}y=y-1;m=m+1;}x=x-1;m=m+1;}
#var₴x=4;if(x$5){x=10;}elif(x#4){x=18;}elif(x$4){x=190;}else{x=45;}
#main_program='var₴x=21;if(x&0){x=10;}elif(x#4&x>20){x=18;}elif(x$4){x=190;}else{x=45;} if(x>12){}'
#main_program='var₴x=f(4+5,8,4+9);'
list_with_token=linker(main_program)
print("main text" ,list_with_token)
parser(list_with_token)
print(var_dict)


       
    




