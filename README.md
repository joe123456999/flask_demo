執行flask
```
source bin/activate

cd server

python app.py
```

ngrok 把server給人家看
```
./ngrok http 5000
```

line bot 流程
1. 執行 Flask
2. 執行 ngrok
3. 把 ngrok https 網址貼到 Line console

參考網站
[Line console message API](https://developers.line.me/en/)