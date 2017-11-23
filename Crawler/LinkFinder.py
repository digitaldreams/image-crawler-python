from html.parser import HTMLParser
import urllib.parse
import functions
from UrlFinder import UrlFinder


class LinkFinder(UrlFinder):
    def __init__(self, page_url):
        super().__init__(self, page_url, 'a', 'href')
