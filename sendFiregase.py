import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# firebaseに取得した情報を送信するクラス
class SendFirebase():
    # インスタンスの引数として、企画者名、開催日、イベントタイトル、概要へのリンクを指定。webLinkはrequiered
    def __init__(self, webLink, companyName = "sendFirebaseTest", date = "sendFirebaseTest", title = "sendFirebaseTest" ) -> None:
        self.companyName = companyName
        self.date = date
        self.title = title
        self.webLink = webLink

    # 実際に送信するためのクラス定義
    def main(self):
        cred = credentials.Certificate("./annoyingadvertisements-63b44-firebase-adminsdk-qf3k6-b1cd2eba56.json") # ダウンロードした秘密鍵
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        data = {"companyName": self.companyName, "date": self.date, "title": self.title, "webLink": self.webLink }
        db.collection("event").add(data)
        print("test")

if __name__ == "__main__":
    sendFirebase = SendFirebase(webLink="testLink")
    sendFirebase.main()