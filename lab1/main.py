from parserr import parser
from constant import *
from parserr import linker

#var q=((4+5)*2)+(7-7.2)/5; помилка
#i=Interpetator("var b=6+8+a+3") 
#i.var_defenition()
# перевірити чому не можна _ використоувавти у функціях
# зробити так щоб можна було писати return -5;
# використання юзер функції всередині іншої юзер функції
# cстворити кдас для юзерфункції
main_program="" 
file = open('text4.txt', 'r')
while 1:
    text=file.readline()    
    #text=input("<input>")
    #list_with_code=text.split("\n")
    #interpretator=Interpretator(text)
                   #interpretator.var_defenition()
    if text=="run":
        break
    else:
         for i in range(len(text)):
             
             if text[i]==" " or text[i]=="\t":
                pass
                 
             else:
                 text=text[i:]
                 print(text)
                 break
         if text[0:len(VAR)]==VAR:
            st=text.replace(" ","")
            if st[len(VAR)]!=EQ:
                text=text[0:len(VAR)]+"₴"+   text[len(VAR):]
         elif text[0:len(FUN)]==FUN:
            st=text.replace(" ","")
            if st[len(FUN)]!=EQ:
                text=text[0:len(FUN)]+"₴"+   text[len(FUN):]
         elif text[0:len(RETURN)]==RETURN:
            st=text.replace(" ","")
            if st[len(RETURN)] not in ["+","-","=","(",")","!"]:
                text=text[0:len(RETURN)]+"₴"+   text[len(RETURN):]
        # print(text)
         main_program+=text
    ##print(var_dict)
#list_with_program=separetor(main_program,"{","}",)
# var₴ x=4;var₴ y=5;var₴ m=0;while(x){if(x$3){m=m+10;}y=5;while(y){if(y$2){m=m+3;}y=y-1;m=m+1;}x=x-1;m=m+1;}
#var₴x=4;if(x$5){x=10;}elif(x#4){x=18;}elif(x$4){x=190;}else{x=45;}
#main_program='var₴x=21;if(x&0){x=10;}elif(x#4&x>20){x=18;}elif(x$4){x=190;}else{x=45;} if(x>12){}'
#main_program='var₴x=f(4+5,8,4+9);'
#main_program="fun₴m(a,b,c){var₴x=4; print(x); if(x#4){return₴type(8);}elif(x>2){return₴float(8);}}  var₴x=10; var₴v=m(4,5,8); print(x);"
#main_program="fun₴m(a){print(a);}  fun₴m(a,b){print(a,b);}  m(2,4);"
file.close()
list_with_token=linker(main_program)
print("main text" ,list_with_token)
parser(list_with_token)
print(var_dict)



       
    




