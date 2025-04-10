# 词频分析
import re
from collections import Counter

def word_frequency_analysis(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        text = text.replace('[!"#$%&()*+-,./:;<=>?@[\\]^_`{|}~]', ' ').replace('.',' ')
        words = text.split()
        counter = Counter(words)
        return counter.most_common(30)

lst = word_frequency_analysis('./Romeo+Juliet.txt')
for index, (word, count) in enumerate(lst, start=1):
    print(f"{index}\t{word}\t{count}")