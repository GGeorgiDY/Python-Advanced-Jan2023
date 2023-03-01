# напиши програма, която чете лист от думи от даден файл и казва колко пъти всяка от думите се съдържа в друг файл.
# мачването трябва да е case insensitive
# резултата го запиши в текстов файл, като сортирай думите по брой съвпадения в обратен ред

import re
pattern = r"[A-Za-z\']+"


def read_target_words(path):
    result = []
    with open(path, 'r') as words_file:
        for line in words_file:
            result.extend(line.split())
    return result


def count_target_words(path, words):
    count_words = {word: 0 for word in words}
    with open(path, 'r') as text_file:
        for line in text_file:
            all_line_words = re.findall(pattern, line)
            for word in all_line_words:
                word_lower = word.lower()
                if word_lower in count_words:
                    count_words[word_lower] += 1
    return count_words

def write_result_to_file(path, count_words_dict):
    sorted_dict = dict(sorted(count_words_dict.items(), key=lambda x: -x[1]))
    with open(path, 'w') as result_file:
        for word, count in sorted_dict.items():
            result_file.write(f"{word} - {count}\n")


target_words = read_target_words('words.txt')
count_words = count_target_words('input.txt', target_words)
write_result_to_file('output.txt', count_words)