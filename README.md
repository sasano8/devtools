
Powershell で以下のコマンドを実行し、自分の ip アドレスを確認する。

```
ipconfig
```

seed.json を作成する。

```
{
    "auth": {
        "domain": "127-0-0-1.sslip.io",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$InQXT1QeVbHaKEGNfX7i6A$rqGKCS2uVrpnx/8VlNNwomKZy/6JxlfMTI02NSjdHhk"
    }
}
```

```
mkdir -p .volumes/authelia
```

```
python3 ./scripts/generate.py
```

```
curl auth.127-0-0-1.sslip.io
```

Windows マシンをサーバーとして公開する場合は、以下のコマンドでプロキシの設定が必要です。
これは、WSL に通信を転送するための設定です。

```
netsh interface portproxy add    v4tov4 listenport=443 listenaddress=0.0.0.0 connectport=443 connectaddress=127.0.0.1
```

プロキシが不要になった場合は、以下のコマンドで削除できます。

```
netsh interface portproxy delete v4tov4 listenport=443 listenaddress=0.0.0.0
```
