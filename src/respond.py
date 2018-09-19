import os
import requests
import json
from importlib import import_module

def reply(bot_id, msg):
    """This function responds to a user request"""
    url = 'https://api.groupme.com/v3/bots/post'

    if is_command(msg) == True:
        command = msg.split()[0][1:]
        arg = msg.split()[1:]
        response = run_module(command, arg)
        send_post(bot_id, response, url)
    elif msg[0]=='-':
        send_post(bot_id,'This command does not exist.',url)
    else:
        return


def is_command(msg):
    """Determines if the message is a command"""

    content = []
    command = msg.split()[0]

    #Parses out commands.txt file
    filename = (os.path.join(os.path.dirname(__file__), 'command.txt'))
    with open(filename) as f:
        for line in f:
            content.append(line.rstrip('\r\n'))

    if command[0]=='-' and command[1:] in content:
        return True
    else:
        return False

def run_module(command, arg):
    module = import_module('src.commands.%s' % (command))
    importlib.reload(module)
    response = module.main(command)
    return response

def send_post(bot_id, msg, url):
        template = {
            'bot_id' : bot_id,
            'text' : msg,
            'attachments' : []
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(template), headers=headers)
