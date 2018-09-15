import flask

app = flask.Flask(__name__)
bot_id = 'c16cfe66242b8d31fb901bce3e'

@app.route('/', methods=['POST'])
def webhook():
    message = flask.request.get_json()
    print('cool cool cool...')
