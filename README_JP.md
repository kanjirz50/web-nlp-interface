# 日本語版README
---
# NLP Webデモ用テンプレート

自然言語処理研究者が研究成果のデモを作成する際のテンプレートです。

このテンプレートをカスタマイズして公開するためには以下の基本的な知識が必用です。
- Python
- HTML
- JavaScript(jquery)
- Webアプリケーション


# 使い方
## まずはデモを動かそう
以下のコマンド群を入力することでローカルでデモを確認できます。

```sh
git clone https://github.com/kanjirz50/web-nlp-interface.git
cd web-nlp-interface
gunicorn -b 127.0.0.1:8080 -w 1 index:app
```

上記コマンドを実行後に127.0.0.1:8080にアクセスするとデモが表示されるはずです。
** gunicorn ** をインストールしていない場合は`pip install gunicorn`でインストールしてください。


## デモをherokuで動かそう
herokuはクラウドアプリケーションのプラットフォームでデモの公開を簡単にします。
このレポジトリを自分のレポジトリへフォークして、それをherokuに登録すると、デモが動作します。

# テンプレートの編集
テンプレートは至って簡単な構造です。
デモ例では、入力はテキスト、出力は[[単語, 小文字化された単語], ...]となります。
テンプレートを編集して自分の手法の入出力に合わせるためには以下の部分を最低限編集する必用があります。

- `static/js/analyze.js`
  - 無名関数: GETリクエストでtextを送る。送るデータはjsonで梱包される。
  - writeTable関数: 受け取った結果をHTML内のTableに書き出す

- `views/contents/demo.html`
  - 結果をTableに表示する。表の見出しや列数を受け取るデータと整合性が取れるように編集する。

# テンプレート応用例
- [Snowman](http://snowman.jnlp.org/english)
  - [Screen capture](https://a13ed10a-a-dee0cc0a-s-sites.googlegroups.com/a/jnlp.org/snowman/snowman/雪だるまH28.4.8.PNG)
  - Japanese word analyzer
  - This analyzer is Web-based system.
- [Vietnamese morphological analyzer](http://160.16.58.116/vietnamese/morph)
  - Provide joint word segmentation and part-of-speech tagging.

# 謝辞
このテンプレートは次のソフトウェアを利用しておりここで感謝の意を示します。
- [Bottle](http://bottlepy.org/docs/dev/index.html) PythonのマイクロWebフレームワーク
- [Bootstrap](http://getbootstrap.com/) HTMLのスタイル

# ライセンス
MIT License, see LICENSE for details.
