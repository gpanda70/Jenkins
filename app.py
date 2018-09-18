import flask
import os
from random import randint
import requests
import json

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
bot_id = '48761c6a5ecbd6c713c2c670ee'

@server.route('/', methods=['POST'])
def webhook():
    message = flask.request.get_json()

    if message['sender_type'] != 'bot':
        reply(message['text'])
        print('wsss')

    return "ok", 200

def reply(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    template = {
        'bot_id' : bot_id,
        'text' : msg,
        'attachments' : []
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(template), headers=headers)

if __name__ == "__main__":
    server.run()
