import wikipediaapi
import time

"""This file represents the wiki command which returns a wikipedia summary article"""

def main(wiki_obj):
    response = return_summary(wiki_obj)
    return response[0:400]

def return_summary(wiki_obj):
    """This function returns a summary of a wikipedia page"""

    wiki_wiki = wikipediaapi.Wikipedia('en')
    time.sleep(3)
    page = wiki_wiki.page(wiki_obj)

    if page.exists() and not check_disambiguous(wiki_obj, page):
        return("Page - Title: %20s\nPage - Summary: %20s" %(page.title, page.summary))
    elif page.exists() and check_disambiguous(wiki_obj, page):
        return('Re-enter your wikipedia search. It is ambiguous.\n\n%s' %(page.text))
    else:
        return('This page doesn\'t exist')

def check_disambiguous(wiki_obj, wiki_page):
    """This functions checks if wikipedia article is disambiguous"""

    d_text = 'may refer to'
    if d_text in wiki_page.summary:
        return True
    else:
        return False

return_summary('Osborn')
