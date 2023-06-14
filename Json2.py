import json
with open("C://Users//susithra.v//Documents//python basic//sample_data (1).json","r")as words:
    readfile=words.read()
data=json.loads(readfile)
list1=[]
key1=data["parametersList"]
print(key1)#it will print all the content in the parameterlist
for i in key1:
    dict1={}
    key2=i["parameterName"]
    print(key2)#we are accessing the values of uisng parameterName key which is BOD,COD,FLOW,TSS,PH.
    val1=i["min"]
    print(val1)
    val2=i["max"]
    print(val2)
    val3=i["avg"]
    print(val3)
    dict1["parameterName"]=key2
    dict1["min"]=val1
    dict1["max"]=val2
    dict1["avg"]=val3
    #print(dict1)
    list1.append(dict1)
print(list1)
with open('C://Users//susithra.v//Downloads//output.json',"w")as output:
    output.write(json.dumps(list1,indent=2))

     
        


    


