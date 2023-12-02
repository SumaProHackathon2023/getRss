# https://connpass.com/explore/ja.atom
# 上のリンクのやつをうまいこと取得できるようにしてほしい
# わかりづらかったら、コメントアウトめちゃめちゃ使っていいよ
import feedparser
import pprint
from uploadFilter import UploadFilter

url = "https://connpass.com/explore/ja.atom"
f = feedparser.parse(url)

uploadFilter = UploadFilter(f)
while True:
    uploadFilter.main()
