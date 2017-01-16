import operator


def load_data(filepath):
    with open(filepath, encoding='utf-8') as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    words_list = text.split()
    words_count = {}
    for item in words_list:
        words_count[item] = words_list.count(item)
    top_words_count = sorted(words_count.items(), key=operator.itemgetter(1),
                             reverse=True)[:10]
    print('Самые частые слова')
    for item in top_words_count:
        print('%s встречается %s раз(а)' % (item[0], item[1]))


def clear_text_from_punctuation(text):
    punctuation_list = list('1234567890!@#$%^&*(){}[];:",./<>?~_=|`\u2014\u002D\u005C\u0027')
    for item in punctuation_list:
        text = text.lower().replace(item, '')
    return text


if __name__ == '__main__':
    filepath = str(input('Введите путь до текстового файла:'))
    get_most_frequent_words(clear_text_from_punctuation(load_data(filepath)))
    
