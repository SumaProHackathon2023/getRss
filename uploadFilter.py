import feedparser

class UploadFilter():

    # コンストラクタ
    def __init__(self, rssData: feedparser.util.FeedParserDict) -> None:
        self.rssData = rssData #呼び出し元から受け取る変数を定義
        self.new_Information = [] # 結果を格納するための変数
        self.rssCash = rssData[0]

    # この関数をgetRss.pyでループして起動してく
    def filtering(self, rssData) -> None:
        for article in self.rssData:
            self.new_Information.append(article)

    def updateRssData(self, rssData):
        if self.rssCash != rssData[0]:
            #print(self.rssCash)
            #print(rssData[0])
            #print("diff")
            # 新しいイベントは何があるかを比較する
            self.differebcingRss(rssData)
            # 出した差分をsendFirebaseで送信処理を実行
            # 差分用のself.rssCashに、新しい差分の一番新しいイベントを入れる
            self.rssCash = rssData[0]
        else:
            print("あってる")

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

if __name__ == '__main__':
    # 確認のためのデータ取得
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    uploadFilter = UploadFilter(f.entries[0].title)
    uploadFilter.filtering(f.entries[1].title)