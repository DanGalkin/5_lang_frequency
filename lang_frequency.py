import re
import sys
from collections import Counter


def load_text_data(filepath):
    '''
    str -> str
    gets the filepath to the file and returns the text from it
    '''
    with open(filepath, encoding='utf-8') as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    '''
    str -> list
    The function finds all words in a string
    and return the list of 10 most common with their frequency
    '''
    words_list = re.findall(r'\w+', text.lower())
    return Counter(words_list).most_common(10)


if __name__ == '__main__':
    try:
        text_filepath = sys.argv[1]
        text = load_text_data(text_filepath)
    except IndexError:
        print('Не указан путь к файлу с текстом, программа завершит работу.')
        sys.exit()
    except FileNotFoundError:
        print('Файл не найден, программа завершит работу.')
        sys.exit()

    top_words_count = get_most_frequent_words(text)
    print('Самые часто встречающиеся слова в тексте:')
    for item in top_words_count:
        print('Слово {:^10} встречается {:5} раз(а)'.format(item[0], item[1]))