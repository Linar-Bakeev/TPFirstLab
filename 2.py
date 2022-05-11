import re

def translate(templ):
    regularEx = ""
    for char in templ:
        if char == '1':
            regularEx += '[бвгджзйклмнпрстфхцчшщ]'
        elif char == '0':
            regularEx += '[ауоыиэяюёе]'
        elif char == '?':
            regularEx += '[а-я]'
        else:
            regularEx += '[а-я]{0,}'
    return regularEx


template = input()
charSt = -1

if template.find('*') != -1:
    charSt = template.find('*')

words = []
line = input()
while line:
    if charSt == -1:
        if re.match(translate(template), line):  # сопоставление строк с шаблоном
            words.append(line)
    elif re.match(translate(template[0:charSt]), line[0:charSt]) \
            and re.match(translate(template[charSt + 1:len(template)]),
                         line[len(line) - (len(template) - (charSt + 1)):len(line)]) \
            and len(line) >= (len(template) - 1):
        words.append(line)
    line = input()

if words:
    for word in words:
        print(word)
else:
    print("Нет результата")
