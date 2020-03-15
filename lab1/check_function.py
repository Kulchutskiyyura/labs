def is_string(string):
       # if len(string)==0:
       #     return False
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

def cheack_if_arguments_is_the_same(arguments_list):
    pass

