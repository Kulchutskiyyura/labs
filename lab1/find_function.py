from constant import*
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

def find_end_of_brackets_index(string,type_of_brackets_first,type_of_brackets_second):
            index=0
            if find_index_of_token(string,type_of_brackets_first,BREAK):
                index=find_index_of_token(string,type_of_brackets_first,BREAK)
            counter=1 
            index_2=index
            end_index=0
            for i in range(index+1,len(string)):
                if string[i]._value==type_of_brackets_first and string[i]._typee==BREAK:
                    counter+=1
                if string[i]._value==type_of_brackets_second and string[i]._typee==BREAK:
                    counter-=1
                if counter==0:
                    index_2=i
                    break
            else:
                print(string)
                print("problem with "+ type_of_brackets_first+" with index " +str(index+1))
                return None
            return index_2
