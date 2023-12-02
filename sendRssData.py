import feedparser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class SendRssData():

    # コンストラクタ
    def __init__(self, rssData: feedparser.util.FeedParserDict) -> None:
        self.rssData = rssData #呼び出し元から受け取る変数を定義
        self.rssCash = rssData[0]

    def sendRssData(self, rssData):
        
        # そもそも更新があるかどうかを判定
        if self.rssCash != rssData[0]:
            # 新しいイベントは何があるかを比較する
            rssDiff = self.differebcingRss(rssData)

            # 出した差分をsendFirebaseで送信処理を実行
            self.setFirebase(rssDiff)

            # 差分用のself.rssCashに、新しい差分の一番新しいイベントを入れる
            self.rssCash = rssData[0]

    def differebcingRss(self, rssData) -> feedparser.util.FeedParserDict:
        """
        rssDataの中から新しいイベントだけを抽出する
        input: 新しく更新されたrssData
        output: rssDataの更新された部分のみ
        """
        print(len(rssData))
        count = 0
        for article in rssData:
            if article != self.rssCash:
                count += 1
                print("yes")
            else:
                print("Noooooooooooooo!!!!!!!!!")
                break
        print(len(rssData[:count]))
        return rssData[:count]

    def setFirebase(self, rssDiff) -> None:
        cred = credentials.Certificate("./annoyingadvertisements-63b44-firebase-adminsdk-qf3k6-b1cd2eba56.json") # ダウンロードした秘密鍵
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        data = [{"companyName": "empty", "date": "empty", "title": newRss.title, "webLink": newRss.link } for newRss in rssDiff]
        db.collection("event").add(data)
        print("test")

if __name__ == '__main__':
    # 確認のためのデータ取得
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    SendRssData = SendRssData(f.entries[0].title)
    SendRssData.filtering(f.entries[1].title)