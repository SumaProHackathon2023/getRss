import feedparser
import time

from sendRssData import SendRssData

# rssDataを取得して、entriesのvalueを抽出
url = "https://connpass.com/explore/ja.atom"
rssData = feedparser.parse(url).entries

# firebaseにあげるためのクラスのインスタンス生成
sendRssData = SendRssData(rssData)

# rssのイベント追加をトリガーに、新しいイベントをfirebaseに送信する
# print(feedparser.parse(url).entries[0].summary[5:30])

while True:
    # rssの取得して、データ送信のための関数を呼び出す
    rssData = feedparser.parse(url).entries
    
    sendRssData.sendRssData(rssData)
    time.sleep(60)

    # デバッグ用
    print("getRss_pass")
    # # 新しいイベントが追加されたかのテスト用 #
    # s = [rssData[len(rssData) - _-1] for _ in range(len(rssData))] #entriesを反転させる
    # sendRssData.sendRssData(s)   #確認
    # time.sleep(60)
