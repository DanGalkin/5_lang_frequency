import re
import sys
from collections import Counter


def load_text_data(filepath):
    with open(filepath, encoding='utf-8') as text_file:
        return text_file.read()


def get_most_frequent_words(text_string, most_common):
    words_list = re.findall(r'\w+', text_string.lower())
    return Counter(words_list).most_common(most_common)


if __name__ == '__main__':
    try:
        text_filepath = sys.argv[1]
        text_string = load_text_data(text_filepath)
    except IndexError:
        print('Не указан путь к файлу с текстом, программа завершит работу.')
        sys.exit()
    except FileNotFoundError:
        print('Файл не найден, программа завершит работу.')
        sys.exit()

    most_common = 10
    top_words_count = get_most_frequent_words(text_string, most_common)
    print('Самые часто встречающиеся слова в тексте:')
    for word in top_words_count:
        print('Слово {:^10} встречается {:5} раз(а)'.format(word[0], word[1]))
