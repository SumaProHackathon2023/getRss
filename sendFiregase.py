import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# firebaseに取得した情報を送信するクラス
class SendFirebase():
    def __init__(self) -> None:
        pass

    # 実際に送信するためのクラス定義
    def main(self):
        cred = credentials.Certificate("./annoyingadvertisements-63b44-firebase-adminsdk-qf3k6-b1cd2eba56.json") # ダウンロードした秘密鍵
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        data = {"companyName": "sendFirebaseTest", "date": "sendFirebaseTest", "title": "sendFirebaseTest", "webLink": "sendFirebaseTest" }
        db.collection("event").add(data)
        print("test")

if __name__ == "__main__":
    sendFirebase = SendFirebase()
    sendFirebase.main()