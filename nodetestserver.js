import {createServer} from 'node:http';
//　このライブラリの読み込みはファイル保存した状態での実行時は成功したが、対話モードでの実行はSyntaxErrorが出ていて、前にも同じ挙動を確認しているため、勉強がどこかで必要と考えます。

const server = createServer((req,res) => {
	res.writeHead(200,{'Contest-Type':'text/plain'});
	res.end('これがWeb上に表示されると、NodeJSを使ったサーバー構築テストが完了\n');
});

server.listen(80,'127.0.0.1',() => {
	console.log('80番ポートでHTTPのリクエストを受け取ることができます');
});

