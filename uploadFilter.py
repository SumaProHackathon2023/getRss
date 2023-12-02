import feedparser

class UploadFilter():
    
    # コンストラクタ
    def __init__(self, rssData: list) -> None:
        self.rssData = rssData #呼び出し元から受け取る変数を定義
        self.new_Information = [] # 結果を格納するための変数

    # この関数をgetRss.pyでループして起動してく
    def filtering(self, rssData) -> None:
        for article in self.f.entries:
            new_Information.append(article)

if __name__ == '__main__':
    # 確認のためのデータ取得
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    uploadFilter = UploadFilter(f.entries[0].title)
    uploadFilter.filtering(f.entries[1].title)