from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('XYn6Q+l4PH/4Z1EWbPq5FYCpJQB+9/HqT6YL3tmCsA5REf5ujdG+iLVZSzdd5IpwOXbDdUUII/N2GrSUWxszZF7WKFjV3T5KL9kmrJXwzJ+8WpG6GdTUN+kkzwY3Cld4Y5AkVHTPH6RpSJXrVX0qOAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('268e9ae8dc7fa0c49d61862e45e751e0')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'hello':
        reply = 'hello Joe'
    else:
        reply = 'your message %s' % event.message.text

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()