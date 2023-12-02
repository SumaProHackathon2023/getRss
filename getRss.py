# https://connpass.com/explore/ja.atom
# 上のリンクのやつをうまいこと取得できるようにしてほしい
# わかりづらかったら、コメントアウトめちゃめちゃ使っていいよ
import feedparser
import pprint
# from uploadFilter import UploadFilter

url = "https://connpass.com/explore/ja.atom"
f = feedparser.parse(url)
rssData = []
# uploadFilter = UploadFilter(rssData)
# while True:
#     uploadFilter.filtering(rssData)
# for article in f.entries:
#     rssData.ap{"nd(coitle": selarticle.title,ebLink": selarticlebl }
 


p# rint(rssData)#print(leen(f))
#ppint.pprint(f)
# file = open('myfile.txt', 'w', encoding = 'UTF-8')
# for article in f.entries:
#     file.write('title:' + article.title + ' ' + 'link:' + article.link)
#     file.write('\n')
# file.close()
