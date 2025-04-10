def count_letters(text):
    text = text.lower()
    letter_counts = [0] * 26
    for char in text:
        if 'a' <= char <= 'z':
            letter_counts[ord(char) - ord('a')] += 1
    # 将列表中的元素和它们对应的字母组合在一起，并按频率降序排序
    sorted_counts = sorted(enumerate(letter_counts), key=lambda x: x[1], reverse=True)
    # 过滤掉频率为0的字母
    non_zero_counts = [(chr(char+ord('a')), count) for char, count in sorted_counts if count > 0]
    return non_zero_counts

text = input("输入一段英文：")
# 调用函数并打印结果
result = count_letters(text)
for char, count in result:
    print(f"'{char}': {count}")