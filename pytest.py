print("pythonのテストコードを書いたのですが、プログラミングの命令をほぼ覚えていないため、プリント命令だけ適当にメッセージを書きながら実行テストしてみます")

print("PC側にサーバーをおいて通信を確立しないとセキュリティの設定上（快活PCの）通信が確立できないことがivcamアプリでわかりました。opensshで試そうと思ったのですが、快活PCのパスワードを獲得することができなかったため、ivcamで快活PCにサーバーを立てて、iPhoneのivcamクライアントアプリを使って通信が確立できることがわかりました。")

print("ここからスマホで実装してたサーバーテンプレを記入")

import http.server
import socketserver

# このパッケージが存在するかpythonコマンドで確認しに行きます。
# pythonコマンドでこのソースをエラーなく実行できたためパッケージは正しく読み込まれてると思われます。一度コミットします。
# コミットが完了したためこのまま実装します。

PORT = 80

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port",PORT)
    httpd.serve_forever()

# これで一時実装しに行きます。
# サーバーの立ち上げは成功しサーバー実装したマシンからはhttpサーバの表示ができたが、スマホから接続できなかったため、実装に使った8000ポートに門で胃がある可能性が一番高いです。この8000番ポートを変更しながら使えるポートを探していきます。ファイヤーフォールは使えませんでした。

