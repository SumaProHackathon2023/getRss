import feedparser
import pprint
import time
from uploadFilter import UploadFilter

url = "https://connpass.com/explore/ja.atom"
rssData = feedparser.parse(url).entries
uploadFilter = UploadFilter(rssData)
rssData = feedparser.parse(url).entries
uploadFilter.updateRssData(rssData)
while True:
    rssData = feedparser.parse(url).entries
    uploadFilter.updateRssData(rssData)
    time.sleep(1)
    # 新しいイベントが追加されたかのテスト用 #
    s = [rssData[len(rssData) - _-1] for _ in range(len(rssData))] #entriesを反転させる
    uploadFilter.updateRssData(s)   #確認
    time.sleep(60)


