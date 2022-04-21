# マンガなどの名言集からありそうな名言(?)を自動生成するAPIです
## 主な仕様
- python3.7
- janome
- markovify（マルコフ連鎖)
- BS4(スクレイピング時に使用)
- flask
- ※ requirements.txtファイルに使用環境入ってますが、使ってないライブラリも多く含まれてます
- HTMLからGETのリクエストがあった時にword_dcdc.pyで処理した結果が返ります。（ローカルサーバー起動しないと動きません）
## これを表現する用のHTMLファイル
- https://github.com/takayanagishinnosuke/manga_meigen_html/blob/main/README.md

## こだわった点
- 固有名詞を結合してみたり、単語の出現頻度からよく使われる単語を除去してみたりしましたが、削りすぎるとマンガ独特の言い回しも削れてしまうので調整に悩みました。
## 改良点
- POSTされたデータによって生成処理に変化を加えたかったが、間に合わず…。
- FlaskとAjaxについてもっと勉強します。
