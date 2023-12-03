import feedparser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class SendRssData():

    # コンストラクタ
    def __init__(self, rssData: feedparser.util.FeedParserDict) -> None:
        self.rssCash = rssData[0]
        cred = credentials.Certificate("./annoyingadvertisements-63b44-firebase-adminsdk-qf3k6-b1cd2eba56.json") # ダウンロードした秘密鍵
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        # self.cacheEvent = self.getFirebaseCache()
        self.setFirebaseCache()
        # print(type(self.cacheEvent))
        print(type(self.rssCash))


    def sendRssData(self, rssData):

        # そもそも更新があるかどうかを判定
        if self.rssCash != rssData[0]:
            # 新しいイベントは何があるかを比較する
            rssDiff = self.differebcingRss(rssData)

            # 出した差分をsendFirebaseで送信処理を実行
            self.setFirebase(rssDiff)

            # 差分用のself.rssCashに、新しい差分の一番新しいイベントを入れる
            self.rssCash = rssData[0]

            # デバッグ用
            print("sendRssData_true")
        else:
            print("sendRssData_false")


    def differebcingRss(self, rssData) -> feedparser.util.FeedParserDict:
        """
        rssDataの中から新しいイベントだけを抽出する
        input: 新しく更新されたrssData
        output: rssDataの更新された部分のみ
        """
        # print(len(rssData))   #入ってきた数
        count = 0
        for article in rssData:
            if article != self.rssCash:
                # print("yes")
                count += 1
            else:
                # print("Noooooooooooooo!!!!!!!!!")
                break
        # print(len(rssData[:count]))   # 更新された数
        return rssData[:count]

    def setFirebase(self, rssDiff) -> None:

        # 更新のある要素一つ一つをfirebaseに送信する
        [self.db.collection("event").add({"companyName": "empty", "date": newRss.summary[5:30], "title": newRss.title, "webLink": newRss.link}) for newRss in rssDiff]
        print("flag_setFirebase")

    def setFirebaseCache(self):
        self.db.collection("cacheEvent").add(self.rssCash)

if __name__ == '__main__':
    # 確認のためのデータ取得
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url).entries
    SendRssData = SendRssData(f)
    # SendRssData.filtering(f.entries[1].title)
