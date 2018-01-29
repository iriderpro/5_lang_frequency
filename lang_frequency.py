from collections import Counter
import re
import sys
import os


def load_data(filepath):
    with open(filepath, 'rt', encoding='utf8') as file_obj:
        list_words = []
        for line in file_obj:
            for word in re.findall(r'\w+', line):
                list_words.append(word)
        return list_words


def get_most_frequent_words(list_words):
    cntr_obj = Counter(list_words)
    most_frequent_words = cntr_obj.most_common(10)
    return most_frequent_words


if __name__ == '__main__':
    if len(sys.argv) == 1 or os.path.exists(sys.argv[1]) is False:
        sys.exit('Не указан входной файл или он не существует')
    frequent_words = get_most_frequent_words(load_data(sys.argv[1]))
    print(frequent_words)
