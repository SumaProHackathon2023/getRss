# getRss

## 必要そうな機能
- rssを持ってくる
- firebaseに送信する
- これを自動化したい
 - webとして公開する
   - streamlit
   - ラズパイ使ってサーバーとして動かす
- 期限切れのやつは削除する

## git 操作
### push
```
git add .
git commit -m 'メッセージ'
git push origin <ブランチ名>
```

### pull
```
git pull origin <ブランチ名>
```

### ブランチ作成
```
git checkout -b <ブランチ名>
```

### ブランチ移動
```
git checkout <ブランチ名>
```

### ブランチの確認
```
git branch
```

### ブランチの削除
```
git branch -d <ブランチ名>
```

### 一つ前のコミットに戻す
```
git reset --soft HEAD^
```
