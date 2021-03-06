import wikipediaapi
import time
from src.error import meme_error

"""This file represents the wiki command which returns a wikipedia summary article"""

def main(wiki_obj):
    response = return_summary(wiki_obj)
    return response

def return_summary(wiki_obj):
    """This function returns a summary of a wikipedia page"""

    wiki_wiki = wikipediaapi.Wikipedia('en')
    time.sleep(3)  # This is called to prevent request crash
    page = wiki_wiki.page(wiki_obj)

    if page.exists() and not check_ambiguous(wiki_obj, page):
        return("Page - Title: %20s\nPage - Summary: %20s" %(page.title, page.summary))
    elif page.exists() and check_ambiguous(wiki_obj, page):
        return('Re-enter your wikipedia search. It is ambiguous.\n\n%s' %(page.text))
    else:
        return('%s doesn\'t exist\n\n%s' % (wiki_obj, meme_error))

def check_ambiguous(wiki_obj, wiki_page):
    """This functions checks if wikipedia article is ambiguous"""

    d_text = 'may refer to'
    if d_text in wiki_page.summary:
        return True
    else:
        return False

#return_summary('Osborn')
