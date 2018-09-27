from bs4 import BeautifulSoup
import requests
import json
from src.error import meme_error

def main(img_search_obj):
    url = "https://www.google.com/search?q=%s&source=lnms&tbm=isch" % img_search_obj
    img_link = get_img_link(url)
    return img_link

def get_img_link(url):
    try:
        r = requests.get(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"})  # Added this header because websites will change content with default python header
        bs = BeautifulSoup(r.text, 'lxml')  #lxml makes it faster!

        img_div = (bs.find('div', class_ = 'rg_meta'))
        img_link = json.loads(img_div.text)['ou']

        return(img_link)

    except AttributeError:
        return('Image does not exist\n\n%s' %(meme_error))
    except requests.exceptions.Timeout:
        return('Your request timed out. Try Again.')
    except requests.exceptions.TooManyRedirects:
        return('The URL for the first image is bad. Contact James. He thought this might happen, but was too lazy to implement a fix.')
    except requests.exceptions.RequestException as e:
        return('Catastrophic error')
