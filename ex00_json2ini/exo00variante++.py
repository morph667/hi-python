import json, os
import os.path

file = "./ex00_json2ini/sample.json"
string = ""

if os.path.exists(file):
    
    with open(file,'r') as file:
        data = json.load(file) # as a dico
        
    for section in data.keys():
        string+= f"[ {section} ] \n"
        sectionElement = data[section]
        for key in sectionElement.keys():
            string += key + " = " + sectionElement[key] + "\n"
        string += "\n"
            
    with open('./ex00_json2ini/file.ini','w') as file: #ecris le resultat dans un fichier .ini
        file.write(string)
        print("job done !")
    
    with open ('./ex00_json2ini/file.ini','r') as file: #lis le resultat dans la console
        print(file.read())
        
else:
    print("file doesn't exist")
    