def separator(string,*args,main_sep=";"):
    list_with_string=[]
    is_sub_str=False
    is_coment=False
    last_index=0
    #print(string)
    string=string.replace("\n","")
    #string.replace(" ","")
    print(string)
    i=0
    while i < len(string):
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
            elif string[i]=='`':
                string=string[:i]+string[i+1:]
                is_coment=True
                i-=1
        else:
            if is_sub_str:
                if string[i]=='"':
                    is_sub_str=False
            if is_coment:
                if string[i]=='`':
                      is_coment=False
                string=string[:i]+string[i+1:]
                i-=1
        i+=1
    return list_with_string
