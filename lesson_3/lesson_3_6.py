# task 6

def int_func(word):
    """принимает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой."""
    for i in word:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            result_word = word.title()
            return result_word
        else:
            return ('Error enter word')


result_list = [int_func(i) for i in (input('Enter text: ').split())]
if ('Error enter word') in result_list:
    print('Error. Your text consists not only of Latin letters')
else:
    print(f"Result text: {' '.join(result_list)}")
