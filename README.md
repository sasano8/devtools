
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
python3 ./scripts/generate.py
```
