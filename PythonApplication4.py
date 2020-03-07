string="((5+9))+7+(8+5)"

index=string.find("(")
counter=1
index_2=index
number=1
for i in range(1,len(string)-1):
    if string[i]=="(":
        counter+=1
    if string[i]==")":
        counter-=1
    if counter==0:
        index_2=i
        break
else:
    print("eror")
string_new=string[index+1:index_2]
string=  string[:index]+"__"+str(number)+string[index_2+1:]
print(string)


