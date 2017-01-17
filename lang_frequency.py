import operator
from collections import Counter

def load_data(filepath):
    with open(filepath, encoding='utf-8') as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    words_list = re.findall('\w+', text.lower())
    return Counter(words_list).most_common(10)


if __name__ == '__main__':
    filepath = str(input('Введите путь до текстового файла:'))
    top_words_count = get_most_frequent_words(load_data(filepath))
    for item in top_words_count:
        print('%s встречается %s раз(а)' % (item[0], item[1]))
