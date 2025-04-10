# def find_roses(sentence):
#     words = sentence.split()
#     rose_indices = [index for index, word in enumerate(words, start=1) if word.lower() == 'rose']
#     return rose_indices

def find_positions(text, word='rose'):
    positions = []
    text = text.lower()
    word_length = len(word)
    position = text.find(word)
    while position != -1:
        positions.append(position)  # 加1是因为索引从0开始，但我们要显示的位置是从1开始的
        position = text.find(word, position + word_length)
    return positions


input_str = input("请输入一段英文:")
#'"Rose is a rose is a rose is a rose." written by Gertrude Stein'
rose_indices = find_positions(input_str,'rose')
print(f'总共有{len(rose_indices)}个玫瑰，出现的序号为：')
for index in rose_indices:
    print(index)