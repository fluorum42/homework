# Вспоминаем работу с файлом. Есть файл, в котором много англоязычных текстовых строк. Считаем частоту встретившихся
# слов в файле, но через функции и map, без единого цикла!
import sys

f = 'Lesson05_Practical03_text.txt'
text = open(f, "r")
string = text.read().split()
result_words = {}


def count_words(word):
    if word in result_words:
        result_words[word] += 1
    else:
        result_words[word] = 1
    return result_words


list(map(count_words, string))
print(result_words)
