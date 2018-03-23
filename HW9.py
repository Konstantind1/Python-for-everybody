"6 вариант(load)"
import re

start = input('начальная директория: ')
finish = input('конечная директория: ')
with open(paradigm.txt,"r", encoding="utf-8") as f:
    text = f.read()
with open(paradigm.txt,"w", encoding="utf-8") as f:
    f.write(str(re.findall("загруж[у]...[^а-я]", text)))
    f.write(str(re.findall("загружа[я]...[^а-я]", text)))
    f.write(str(re.findall("загружа[ем]...[^а-я]", text)))
    f.write(str(re.findall("загруз[ив]...[^а-я]", text)))
    f.write(str(re.findall("загруз[и]...[^а-я]", text)))
    f.write(str(re.findall("загруз[ил]...[^а-я]", text)))
    f.write(str(re.findall("загруз[или]...[^а-я]", text)))
if not f.writable:
    print("Sorry, this word doesn't exist, please, try again")
