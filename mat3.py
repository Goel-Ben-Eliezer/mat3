file=input("enter file: ")
file=open(file, encoding='UTF-8')
file=file.read()
file=file.splitlines()

#step 1 - Create a dictionary for names and numbers with their ID
i=1
names=dict()
for line in file:
    x=line.find('-')
    y=line.find(":", x)
    
    if line[x+2:y] not in names and y>0 :
            names[line[x+2:y]]=i
            i=i+1

#step 2 - Create a dictionary for messages          
messages=list()
k=0
for line in file:
    a=line.find('-')+2
    b=line.find(':', a)
    
    if b>0:
        messages.append(dict())
        messages[k]['datetime']=line[0:a]
        messages[k]['id']=names[line[a:b]]
        messages[k]['text']=line[b:]
        k=k+1      

#step 3 - Create a dictionary for metadata
metadata=dict()
m=file[1].find('"')+1
n=file[1].find('"', m)
metadata['chat_name']=file[1][m:n]
m=file[1].find('-')-1
metadata['creation_date']=file[1][:m]
metadata['num_of_participants']=len(names)
m=file[1].rfind(' ')+1
metadata['creator']=file[1][m:]

#step 4 - Create a dictionary that includes the metadata and messages
data=dict()
data['metadata']=metadata
data['messages']=messages

# step 5 - convert to json
import json
json_data=metadata['chat_name'] +".txt"
with open(json_data, 'w', encoding='utf8') as json_data:
    json.dump(data, json_data, ensure_ascii=False)



