import feedparser

class UploadFilter():
    def __init__(self, f: feedparser.util.FeedParserDict) -> None:
        self.f = f

    def main(self) -> None:
        print(self.f.entries[0].title)

if __name__ == '__main__':
    # 確認のためのデータ取得
    url = "https://connpass.com/explore/ja.atom"
    f = feedparser.parse(url)
    uploadFilter = UploadFilter(f)
    uploadFilter.main()