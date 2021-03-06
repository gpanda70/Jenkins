import os
import requests
import json
import importlib
from importlib import import_module


def reply(bot_id, msg):
    """This function responds to a user request"""
    url = 'https://api.groupme.com/v3/bots/post'

    # This block is for regular responses
    if is_command(msg):
        command = msg.split()[0][1:]
        arg = msg.split()[1:]
        arg = ' '.join(arg)
        response = run_module(command, arg)
    elif msg[0] == '-':
        send_groupme_message(bot_id, url, msg='This command does not exist.\nCheck -help')
    else:
        return

    # Custom block for WolframAlpha responses that hecks to see if response
    # is a list of urls
    if isinstance(response, list):
        for num, r in enumerate(response):
            png = image_service_process(r, num+1)
            png = {'type': 'image', 'url': png}
            send_groupme_message(bot_id, url, png=png)
    else:
        send_groupme_message(bot_id, url, response)


def is_command(msg):
    """Determines if the message is a command"""
    first_word = msg.split()[0]
    command_symbol = first_word[0]  # command_symbol should be '-'
    command = first_word[1:]  # the command should be a command in command.txt

    filename = (os.path.join(os.path.dirname(__file__), 'command.txt'))
    with open(filename) as f:
        command_list = [line.rstrip('\r\n') for line in f]

    is_command = command_symbol == '-' and command in command_list
    return is_command


def run_module(command, arg):
    """Imports the module that stores the commands and runs it"""

    module = import_module('src.commands.%s' % (command))
    importlib.reload(module)
    response = module.main(arg)
    return response


def send_post(bot_id, url, msg='', png=None):
    """Sends post request,containing command response, to the Groupme-Chat"""

    attachment = []
    if png:
        attachment.append(png)

    template = {
        'bot_id': bot_id,
        'text': msg,
        'attachments': attachment
    }
    headers = {'content-type': 'application/json'}
    requests.post(url, data=json.dumps(template), headers=headers)


def send_groupme_message(bot_id, url, msg='', png=None):
    SPLIT_SIZE = 1000
    if len(msg) > SPLIT_SIZE:
        # This is the best way to get api data with limited number of returns
        split_message_list = [msg[i:i+SPLIT_SIZE] for i in range(0, len(msg), SPLIT_SIZE)]
        for split_message in split_message_list:
            send_post(bot_id, url, split_message)
    else:
        send_post(bot_id, url, msg=msg, png=png)


def save_images(png_link, num):
    """Saves the Wolfram image to ask_images directory"""
    head_path = os.path.dirname(__file__)
    wolf_img_path = 'ask_images/image{}.png'.format(num)
    with open(os.path.join(head_path, wolf_img_path), 'wb') as handle:
        r = requests.get(png_link, stream=True)
        for block in r.iter_content(1024):
            handle.write(block)


def process_image(access_token, num):
    """
    Opens the Wolfram image and then sends it to the Groupme Image Service.
    """
    head_path = os.path.dirname(__file__)
    wolf_img_path = 'ask_images/image{}.png'.format(num)
    with open(os.path.join(head_path, wolf_img_path), 'rb') as handle:
        data = handle
        headers = {'X-Access-Token': access_token, 'Content-Type': 'image/png'}
        png_response = requests.post('https://image.groupme.com/pictures',
                                     headers=headers,
                                     data=data)
        return png_response


def image_service_process(png_link, num):
    """
        This function saves the wolframalpha image and processes them
        through Groupme's image service.
    """
    access_token = os.getenv('access_token')

    save_images(png_link, num)
    png_response = process_image(access_token, num)

    png_link = json.loads(png_response.content)['payload']['picture_url']
    # payload = {'type': 'image', 'url': png}
    return(png_link)
