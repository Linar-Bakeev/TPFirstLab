alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
step = int(input('Шаг шифровки = '))
msg = input('Введите сообщение: ')
res = ''

for i in msg:
    Position = alphabet.find(i)
    NewPos = Position + step
    if i in alphabet:
        res += alphabet[NewPos]
    else:
        res += i
print(res)
