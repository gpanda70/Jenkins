import requests
import json
from importlib import import_module

def reply(bot_id, msg):
    """This function responds to a user request"""
    url = 'https://api.groupme.com/v3/bots/post'

    if is_command(msg) == True:
        command = msg.split()[0][1:]
        run_module(bot_id, command)
    else:
        send_post('This command does not exist.')


def is_command(msg):
    """Determines if the message is a command"""

    content = []
    command = msg.split()[0]

    #Parses out commands.txt file
    with open(command.txt) as f:
        for line in f:
            content.append(line)

    if command[0]=='-' and command[1:] in content:
        return True
    else:
        return False

def run_module(bot_id, command):
    module = import_module('src.commands.%s' % (command))
    importlib.reload(module)
    response = module.main(command)
    send_post(response)

def send_post(bot_id, msg):
        template = {
            'bot_id' : bot_id,
            'text' : msg,
            'attachments' : []
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(template), headers=headers)
