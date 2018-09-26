import os
import requests
import json
import math
import importlib
from importlib import import_module

def reply(bot_id, msg):
    """This function responds to a user request"""

    url = 'https://api.groupme.com/v3/bots/post'

    # If the groupme message is a command it first split the text.
    # Next, it runs the command and stores the response to the command.
    # It then checks if the response returns a list(multiple images) or a single response.
    # It then sends a POST request to your group.
    if is_command(msg) == True:
        command = msg.split()[0][1:]
        arg = msg.split()[1:]
        arg = ' '.join(arg)
        response = run_module(command, arg)

        # Checks to see if response is a list of urls
        if isinstance(response, list):
            for num, r in enumerate(response):
                png = image_service_process(r,num+1)
                gif = {'type': 'image', 'url': png}
                send_post(bot_id, url, gif=gif)
        else:
            split_message_send(bot_id, url, response)
    elif msg[0]=='-':
        send_post(bot_id, url, msg='This command does not exist.\nCheck -help')
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
    """Imports the module that stores the commands and runs it"""

    module = import_module('src.commands.%s' % (command))
    importlib.reload(module)
    response = module.main(arg)
    return response

def send_post(bot_id, url, msg='', gif=None):
    """Sends post request,containing command response, to the Groupme-Chat"""

    attachment = []
    if gif:
        attachment.append(gif)

    template = {
        'bot_id' : bot_id,
        'text' : msg,
        'attachments' : attachment
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(template), headers=headers)

def split_message_send(bot_id, url, msg=''):
    """
        Sends post request, containing command response, to the groupme
        when the length of the message is greater than 10000
    """

    if len(msg)<=1000:
        send_post(bot_id, url, msg=msg)
    else:
        loops = int(math.ceil(len(msg) / 1000))
        start=0
        end=1000

        for loop in range(0,loops):
            send_post(bot_id, url, msg[start:end] )
            start=end

            if end+1000<len(msg):
                end = end+1000
            else:
                end = len(msg) - 1

def image_service_process(gif_link, num):
    """This function processes a list of images through Groupme's image service"""
    access_token = os.getenv('access_token')

    with open(os.path.join(os.path.dirname(__file__), 'ask_images/image{}.png'.format(num)),'wb') as handle:
        r = requests.get(gif_link,stream=True)
        for block in response.iter_content(1024):
            handle.write(block)

    with open(os.path.join(os.path.dirname(__file__), 'ask_images/image{}.png'.format(num)),'rb') as handle:
        data = handle
        headers = {'X-Access-Token': access_token,'Content-Type': 'image/png'}
        gif_response = requests.post('https://image.groupme.com/pictures', headers=headers, data=data)

    png_link = json.loads(gif_response.content)['payload']['picture_url']
    #payload = {'type': 'image', 'url': png}
    return(png)
