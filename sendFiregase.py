import firebase_admin
from firebase_admin import firestore

# firebaseに取得した情報を送信するクラス
class SendFirebase():
    def __init__(self) -> None:
        pass

    # 実際に送信するためのクラス定義
    def main(self):
        app = firebase_admin.initialize_app()
        db = firestore.client()
        data = {"companyName": "sendFirebaseTest", "date": "sendFirebaseTest", "title": "sendFirebaseTest", "webLink": "sendFirebaseTest" }
        db.collection("event").add(data)
        print("test")

if __name__ == "__main__":
    sendFirebase = SendFirebase()
    sendFirebase.main()