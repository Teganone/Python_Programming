import jieba
from wordcloud import WordCloud
from imageio import imread

f = open("2024复旦开学典礼校长讲话-学会持续创新.txt",'r',encoding='utf-8')
txt0 = f.read()

words = ' '.join(jieba.lcut(txt0))
heartmask = imread("./心型.png")

# //stopwords
with open('./hit_stopwords.txt','r',encoding='utf-8') as f:
    stopwords = f.readlines()
    stopwords = [l.strip() for l in stopwords]

# wordcloud
cloud = WordCloud(background_color="white",
                  max_words=100,
                  font_path="simkai.ttf",
                  stopwords=stopwords,
                  mask=heartmask,
                  ).generate(words)
cloud.to_file("./校长讲话.png")