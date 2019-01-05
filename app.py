from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('cbz0++RSqdxMdAG/Og9ecolBmxB4nO7kmY+GgrJKcXdUGednfD6F8y9UXGO75fJTWDpFAlJlpDzZelrbnHKbuREW2NenjTVKrXoPBx+L34/VViPhqi9MQEAKFHcGLs84cFgdjfUFvNcIPnEIc49oqwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c24bb643b8e8ad6010eb878a22539282')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '很抱歉，我聽不懂你說什麼'

    if msg in ['Hi', 'hi', '你好', '您好', '妳好']:
        r = '嗨, 您好'
    elif msg == '早安':
        r = '早安'
    elif msg == '午安':
        r = '午安'
    elif msg in ['晚安', '快睡吧']:
        r = '晚安'
    elif msg in ['who are you', '你是誰', '名字']:
        r = '我是聰明又可愛的Relika機器人'
    elif msg in ['為什麼還不睡']:
        r = '我正在學怎麼做出一個機器人啊'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))
    return

    if msg in ['你好棒', '棒']:
    sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='120'
)

    line_bot_api.reply_message(
        event.reply_token,
        sticker_message)


if __name__ == "__main__":
    app.run()