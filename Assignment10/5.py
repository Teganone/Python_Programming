# 红楼梦
import jieba
import re

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    words = jieba.cut(text)
    unique_words = set(words)
    punctuation = '。，、？！：；“”《》——……'
    unique_words = {word for word in unique_words if word not in punctuation and not re.match(r'\d', word)}
    return len(unique_words)

# 假设文件名为 红楼梦.txt
print(f"《红楼梦》中包含的词汇量：{count_words('红楼梦.txt')}个。")