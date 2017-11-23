from Image import Download
from functions import *
from UrlFinder import UrlFinder

if __name__ == '__main__':
    PAGE_URL = 'http://www.indianexpress.com'
    link = UrlFinder(page_url=PAGE_URL, tag='a', attr='href')
    print(link.page_url)
    #link.feed(link.html_string())
    #print(link.get_values())
