import flask
import os
from random import randint
from src.respond import reply

# Global Variables
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
bot_id = os.getenv('bot_id')


@server.route('/', methods=['POST'])
def webhook():
    """
        This function is called whenever the app's callback URL receives a POST
        In other words whenever a message is sent.
    """
    message = flask.request.get_json()  # This function contains a

    if message['sender_type'] != 'bot':
        reply(bot_id, message['text'])

    return "ok", 200


if __name__ == "__main__":
    server.run()
