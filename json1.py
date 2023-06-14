import json
with open('C://Users//susithra.v//Downloads//words.json',"r",encoding="utf-8")as words:
    readfile=words.read()
data=json.loads(readfile)#[{}{}{}]#convrted to dictionary
dict_1={}
dict_2={}
for i in data:
    key=i["word"]#home,stone,space  access using word key .
    print(key)#it will print home, stone,space, 
    temp=i["meanings"]#we want noun 
    print(temp)#parts of speech :noun ,this and all there in meanings #meaning
    for j in temp: #inside this meaning keyword noun there for that again iteration doing
        
        key_2=j["partOfSpeech"]#noun
        print(key_2)#noun
        value_2=j["definitions"]#list of explanation in definitions keyword.
        print(value_2)#definitions
        list_1=[]
        for z in value_2:
            list_1.append(z["definition"])
        print(list_1)
        dict_1[key_2]=list_1
        print(dict_1)
    dict_2[key]=dict_1
    print(dict_2)
with open('C://Users//susithra.v//Downloads//wo.json',"w")as wor:
    wor.write(json.dumps(dict_2,indent=2))
    

            




    

    





       
        

        
            




    

    



