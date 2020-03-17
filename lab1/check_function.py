def is_string(string):
        if len(string)==0:
           print("\n\n empty string!!!!\n\n\n")
           return False
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
def cheack_if_can_be_var(string):
    for i in string:
        if (i.isalnum() or i in ["_"]) :
            pass
        else:
            return False
    return True
def cheack_if_arguments_is_the_same(arguments_list):
    argument_name_list=[i[0]._value for i in arguments_list]
    for i in range(len( argument_name_list)):
        if argument_name_list[i] in argument_name_list[i+1:]:
            return True
    return False


