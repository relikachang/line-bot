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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飯了嗎?'))


if __name__ == "__main__":
    app.run()