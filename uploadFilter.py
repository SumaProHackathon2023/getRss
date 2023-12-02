import feedparser

class UploadFilter():

    # コンストラクタ
    def __init__(self, rssData: feedparser.util.FeedParserDict) -> None:
        self.rssData = rssData #呼び出し元から受け取る変数を定義
        self.new_Information = [] # 結果を格納するための変数
        self.rssCash = rssData

    # この関数をgetRss.pyでループして起動してく
    def filtering(self, rssData) -> None:
        for article in self.rssData.entries:
            self.new_Information.append(article)

    def updateRssData(self, rssData):
        if self.rssCash[0] != rssData[0]:
            print(self.rssCash[0])
            print(rssData[0])
            print("diff")
            # 新しいイベントは何があるかを比較する
            # 出した差分をsendFirebaseで送信処理を実行
            # 差分用のself.rssCashに、新しい差分の一番新しいイベントを入れる
            # self.rssCash = rssData.entries[0]
        else:
            print("あってる")


if __name__ == '__main__':
    # 確認のためのデータ取得
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    uploadFilter = UploadFilter(f.entries[0].title)
    uploadFilter.filtering(f.entries[1].title)