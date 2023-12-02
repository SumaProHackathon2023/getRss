import feedparser
import pprint
import time
from uploadFilter import UploadFilter

# rssDataを取得して、entriesのvalueを抽出
url = "https://connpass.com/explore/ja.atom"
rssData = feedparser.parse(url).entries

# firebaseにあげるためのクラスのインスタンス生成
uploadFilter = UploadFilter(rssData)

# rssのイベント追加をトリガーに、新しいイベントをfirebaseに送信する
while True:
    # rssの取得して、データ送信のための関数を呼び出す。
    rssData = feedparser.parse(url).entries
    uploadFilter.updateRssData(rssData)
    time.sleep(1)

    # 新しいイベントが追加されたかのテスト用 #
    s = [rssData[len(rssData) - _-1] for _ in range(len(rssData))] #entriesを反転させる
    uploadFilter.updateRssData(s)   #確認
    time.sleep(60)


