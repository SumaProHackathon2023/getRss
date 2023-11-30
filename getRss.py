# https://connpass.com/explore/ja.atom
# 上のリンクのやつをうまいこと取得できるようにしてほしい
# わかりづらかったら、コメントアウトめちゃめちゃ使っていいよ
import feedparser
import pprint

url = "https://connpass.com/explore/ja.atom"
f = feedparser.parse(url)
#print(len(f))
#pprint.pprint(f)
file = open('myfile.txt', 'w', encoding = 'UTF-8')
for article in f.entries:
    file.write('title:' + article.title + ' ' + 'link:' + article.link)
    file.write('\n')
file.close()