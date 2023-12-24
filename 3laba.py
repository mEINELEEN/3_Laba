text = input('Введите любую строку')
example = input('Введите букву, которая послужит образцом')
konectext = ''
splittext = text.split()
for i in range(0,len(splittext)):
    slovo = list(splittext[i])
    if slovo[0] in example and slovo[-1] in example:
        konectext += ' ' + splittext[i]
print(konectext.split(','))

