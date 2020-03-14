from constant import*
from token import Token
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
def find_function_argument(list_with_token):
    print(list_with_token)
    #var x=print(print(5));
    if list_with_token[0]._typee!=FUNCTION:
        return None
    list_with_token=list_with_token[1:]
    index=0
    list_with_argument=[]
    end=False
    if len(list_with_token)==0:
        end=True
    while end==False:
        print("while find argument  ",list_with_token)
        if list_with_token[index]._typee==FUNCTION:
            index_2=find_end_of_brackets_index(list_with_token[index:],"(",")")
            if index_2+1<len(list_with_token):
                index_2+=1
            else:
                index_2+=1
                end=True
            
        elif find_index_of_token(list_with_token,",",BREAK)!=-1:
            index_2=find_index_of_token(list_with_token,",",BREAK)
            
            
        else:
            index_2=len(list_with_token)
            end=True
        print("index  index_2",index,index_2)
        if index!=index_2:
            list_with_argument.append(list_with_token[index:index_2])
        else:
            list_with_argument.append([list_with_token[index]])
        list_with_token=list_with_token[index_2+1:]
        #index=index_2
    print("find_argument ",list_with_argument)
    return list_with_argument
        
