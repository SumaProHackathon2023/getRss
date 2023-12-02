# https://connpass.com/explore/ja.atom
# 上のリンクのやつをうまいこと取得できるようにしてほしい
# わかりづらかったら、コメントアウトめちゃめちゃ使っていいよ
import feedparser
import pprint

def getRss():
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    #print(len(f))
    #pprint.pprint(f)
    file = open('myfile.txt', 'w', encoding = 'UTF-8')
    for article in f.entries:
        file.write('title:' + article.title + ' ' + 'link:' + article.link + " 開催日時:"+article.summary[5:30] + " 更新日時:"+article.updated)
    
        print()
        file.write('\n')
    file.close()
    return f.entries
if __name__ == "__main__":
     getRss()