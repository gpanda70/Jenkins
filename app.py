import flask
import os

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
bot_id = 'c16cfe66242b8d31fb901bce3e'

@server.route('/', methods=['POST'])
def webhook():
    message = flask.request.get_json()
    print('cool cool cool...')
