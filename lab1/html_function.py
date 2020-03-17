
from constant import *
from Token import Token
import urllib.request
#print(data)


def help(text):
    st=''
    i=0
    while  i <  len(text):
        if text[i]=="<":
            i=i+1
            st+='"'
            while(text[i]!=">"):
                st+=text[i]
                i=i+1
            st+='",'
        i=i+1
    return st
def get_page(url,user_use=False):
    web =urllib.request.urlopen(url)
    data=str(web.read())
    data=data[2:-1]
    if user_use:
        return Token(data,STRING)
    return data
def find_tag(tag_name,text,tag_number,return_begin_end_index=False,user_use=False):
    index_in_tag_name=0
    index_in_text=0
    is_string=False  
    index_of_tag_begin=0
    index_of_tag_end=0
    begin_tag_sign_find=False
    tag_find=False
    nothing_find=False
    i=0
    while i<tag_number:
        index_of_tag_begin=index_of_tag_end
        while index_in_text <len(text):
            if not is_string:
                if begin_tag_sign_find:
                    if text[index_in_text]==">":
                        index_of_tag_end=index_in_text
                        break
                else:
                    if text[index_in_text]=="<":
                        if get_tag_type(text[index_in_text+1:])==tag_name:
                            begin_tag_sign_find=True
                            index_of_tag_begin=index_in_text
                            index_in_text+=len(tag_name)
                       
                        #print("index beg",index_of_tag_begin)
                if text[index_in_text]=='"' :
                    is_string=True
            else:
                if text[index_in_text]=='"':
                    is_string=False
            index_in_text+=1
        else:
            nothing_find=True

        if nothing_find:
            break
        else:
            begin_tag_sign_find=False
            tag_find=False
            nothing_find=False
            i+=1
    if nothing_find:
        return None
    elif return_begin_end_index:
        return [index_of_tag_begin,index_of_tag_end]
    elif user_use:
        return Token(text[index_of_tag_begin:index_of_tag_end+1],STRING)
    return text[index_of_tag_begin:index_of_tag_end+1]

def get_tag_type(text,user_use=False):
    #print("text in fun=",text[0:20])
    if text[0]=="<":
        text=text[1:]
    index_of_tad_name_begin=0
    for i in range(len(text)):
        if text[i] not in [" ","\r","\n"]:
            index_of_tad_name_begin=i
            break
    print( index_of_tad_name_begin)
    idex_of_tag_name_end=index_of_tad_name_begin
    for i in range(len(text[index_of_tad_name_begin:])):
        if text[i] in [" ","\r","\n",">"]:
            idex_of_tag_name_end=i
            break
    return_value=text[index_of_tad_name_begin:idex_of_tag_name_end].replace(" ","")
    print("return of fun =",return_value)
    if user_use:
        return Token(return_value,STRING)
    return  return_value

def find_tag_with_html(tag_name,text,tag_number,user_use=False):
    list_with_tag_index= find_tag(tag_name,text,tag_number,return_begin_end_index=True)
    print("\n\n\n\n",list_with_tag_index,"\n\n\n\n")
    counter_of_open_tag=0
    counter_of_end_tag_sign=0
    print(" data sfter find tag ",text[ list_with_tag_index[0]: list_with_tag_index[1]+1])
    print("fun",get_tag_type(text[list_with_tag_index[0]+1:list_with_tag_index[1]+1]),"len=",len(get_tag_type(text[list_with_tag_index[0]+1:list_with_tag_index[1]+1])))
    if get_tag_type(text[list_with_tag_index[0]+1:list_with_tag_index[1]+1]) not in pair_tag:
        print ("eroror not pair tag")
    
    i=list_with_tag_index[1]
    while i < len(text):
        if text[i]=="<" and text[i+1]!="/":
            if get_tag_type(text[i+1:]) in pair_tag:
                 print("fun is loop=",get_tag_type(text[i+1:]))
                 counter_of_end_tag_sign+=1
        elif text[i]=="<" and text[i+1]=="/":
            if counter_of_end_tag_sign==0:
                 list_with_tag_index[1]=i
                 break
            else:
                counter_of_end_tag_sign-=1
        i=i+1
    print("list after loop",list_with_tag_index)
    list_with_tag_index[1]+=text[list_with_tag_index[1]:].find(">")
    print(list_with_tag_index[0],list_with_tag_index[1])
    if user_use:
        return Token(text[list_with_tag_index[0]:list_with_tag_index[1]+1],STRING)
    return text[list_with_tag_index[0]:list_with_tag_index[1]+1]
#print(find_tag("div",data,1))
#print(find_tag_with_html("div",data,4))
#print(fun('<img class="mb16" src="https://cdn.sstatic.net/Img/home/public-qa.svg?v=d82acaa7df9f">'))
#file.write(help(text))
