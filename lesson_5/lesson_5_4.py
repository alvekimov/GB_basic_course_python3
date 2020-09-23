from googletrans import Translator

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as f:
    dict = {}
    for line in f:
        dict[int(line.split(' - ')[1])] = line.split(' - ')[0]
    for key, val in dict.items():
        dict[key] = (translator.translate(val, src='en', dest='ru')).text

with open('text_4_new.txt', 'w', encoding='utf-8') as f:
    for key, val in dict.items():
        f.writelines(f'{val} - {key}\n')
