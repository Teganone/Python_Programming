import re


def save_agent(msg):
    # 假设特工名字由两个或三个中文字符组成，且前面有“特工”二字
    # 使用正则表达式匹配特工名字，并用*替代
    return re.sub(r'特工[\u4e00-\u9fa5]{2,3}', lambda x:  x.group()[2:3] + '*'*len(x.group()[3:]), msg)

# 测试
msg = '特工张大三让特工李小四把图纸USB交给特工王二麻。'
print(save_agent(msg))
