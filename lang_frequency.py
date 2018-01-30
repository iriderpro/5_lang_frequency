from collections import Counter
import re
import sys
import os


def load_data(filepath):
    with open(filepath, 'rt', encoding='utf8') as file_obj:
        str_words_low = file_obj.read().lower()
    return str_words_low


def get_most_frequent_words(str_words):
    list_words = re.findall(r'\w+', str_words)
    Counter_obj = Counter(list_words)
    amount_frequent_words = 10
    most_frequent_words = Counter_obj.most_common(amount_frequent_words)
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) == 1 or os.path.exists(sys.argv[1]) is False:
        sys.exit('Не указан входной файл или он не существует')
    frequent_words = get_most_frequent_words(load_data(sys.argv[1]))
    print('Самые частые слова в тексте', frequent_words)
