import os
import giphy_client
from giphy_client.rest import ApiException
import time
import requests
import json

api_instance = giphy_client.DefaultApi()
giphy_api_key = os.getenv('giphy_api_key')

def main(msg):
    if msg.split()[0] == '-random':
        random = msg.split()
        random = ' '.join(random[1:])
        gif = get_random_gif(random)
    else:
        gif = get_gif(msg)
    return gif

def get_gif(gif_query):
    limit = 1
    offset = 0
    lang = 'en'
    fmt = 'json'
    try:
        api_response = api_instance.gifs_search_get(giphy_api_key, gif_query,
                                                    limit=limit,
                                                    offset=offset,
                                                    lang=lang,
                                                    fmt=fmt)
        gif = api_response.data[0]
        gif_url = gif.images.downsized.url
        return(gif_url)
    except ApiException as e:
        return ('Exception when calling DefaultApi->gifs_search_get: %s\n' %e)
    except AttributeError as e:
        return ('Exception when calling DefaultApi->gifs_random_get: %s\n' %e)

def get_random_gif(gif_query):
    fmt = 'json'
    try:
        api_response = api_instance.gifs_random_get(giphy_api_key, tag=gif_query,
                                                    fmt=fmt)
        gif = api_response.data
        gif_url = gif.fixed_height_downsampled_url
        return(gif_url)
    except ApiException as e:
        return ('Exception when calling DefaultApi->gifs_random_get: %s\n' %e)
    except AttributeError as e:
        return ('Exception when calling DefaultApi->gifs_random_get: %s\n' %e)
