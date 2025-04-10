import re
from collections import Counter

def text_statistics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 统计段落数（回车结束）
    paragraphs = text.split('\n')
    paragraph_count = len(paragraphs)
    
    # 统计句数（.?!结束）
    sentences = re.split(r'[.?!]', text)
    sentence_count = len(sentences) - 1  # 减去最后一个空字符串
    
    # 统计单词数
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    # 统计单词出现的频率，并输出前10个单词
    word_freq = Counter(words)
    top_10_words = word_freq.most_common(10)
    
    return paragraph_count, sentence_count, word_count, top_10_words

# 测试
file_path = './Pumas.txt'
paragraph_count, sentence_count, word_count, top_10_words = text_statistics(file_path)
print(f'段落数：{paragraph_count}')
print(f'句数：{sentence_count}')
print(f'单词数：{word_count}')
print('前10个单词及其频率：')
for word, freq in top_10_words:
    print(f'{word}: {freq}')