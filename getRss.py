# https://connpass.com/explore/ja.atom
# 上のリンクのやつをうまいこと取得できるようにしてほしい
# わかりづらかったら、コメントアウトめちゃめちゃ使っていいよ
import feedparser
import pprint
from uploadFilter import UploadFilter

url = "https://connpass.com/explore/ja.atom"
rssData = feedparser.parse(url).entries
uploadFilter = UploadFilter(rssData)
# pprint.pprint(rssData)

rssData = feedparser.parse(url).entries
uploadFilter.updateRssData(rssData)
while True:
    rssData = feedparser.parse(url).entries
    uploadFilter.updateRssData(rssData)

# print(rssDta)

#print(len(f))

# file = open('myfile.txt', 'w', encoding = 'UTF-8')
# for article in f.entries:
#     file.write('title:' + article.title + ' ' + 'link:' + article.link)
#     file.write('\n')
# file.close()
