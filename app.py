# encoding: utf-8
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

line_bot_api = LineBotApi('7VsCEpcmc1iZ4MQ6PFyuTPDJtO1FXKOTjKVksySsut4ypcCJiQgOEjYTYK1voX89N3yRK0pLzptV3oL5HCY6L1fbwijR5LXwZ3FjVWjoL6Wri9j+y4PZdwE9cwvfqbu2OTPSFRxqd5acxV6aFqMiYwdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('935fcc42269a80c3fb5679b92bb7e7b0') #Your Channel Secret

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
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])