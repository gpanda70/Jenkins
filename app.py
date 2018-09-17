import flask
import os
from random import randint
import requests
import json

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
bot_id = 'c16cfe66242b8d31fb901bce3e'

@server.route('/', methods=['POST'])
def webhook():
    message = flask.request.get_json()
    reply('cool cool cool...')

def reply(msg):
	url = 'https://api.groupme.com/v3/bots/post'
	template = {
		'bot_id'		: bot_id,
		'text'			: msg
	}
    headers = {'content-type': 'application/json'}
    response = requests.post("https://api.groupme.com/v3/bots/post", data=json.dumps(template), headers=headers)
