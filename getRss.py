# https://connpass.com/explore/ja.atom
# 上のリンクのやつをうまいこと取得できるようにしてほしい
# わかりづらかったら、コメントアウトめちゃめちゃ使っていいよ
import feedparser
import pprint
import io, sys
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')



def getRss(last_updated):
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    
    rssData = {}
    # 更新がされているか判定
    if last_updated != f.entries[0].updated:
        for article in f.entries:
            # 更新前の箇所かの判定
            if article.updated != last_updated:
                #タイトルをキーとする辞書を作成valueにはlinkと開催日、更新日を空白区切りで
                rssData[article.title] = article.link +" "+ article.summary[5:30]+" "+article.updated
            else:
                break
        last_updated = f.entries[0].updated
        print(last_updated)
        return rssData, True, last_updated
    return "", False, last_updated


if __name__ == "__main__":
    last_updated = ""

    for i in range(10): #とりあえず10回
        rssData, update, last_updated = getRss(last_updated)
        print(update)
        #if update:
        #   print(rssData)
        time.sleep(1)
    """
    rssData, last_updated = getRss(last_updated)
    print(rssData)
    time.sleep(1)
    rssData, last_updated = getRss(last_updated)
    print(rssData)
    time.sleep(1)
    """


# print(rssData)
#print(leen(f))
#pprint.pprint(f)
# file = open('myfile.txt', 'w', encoding = 'UTF-8')
# for article in f.entries:
#     file.write('title:' + article.title + ' ' + 'link:' + article.link)
#     file.write('\n')
# file.close()
