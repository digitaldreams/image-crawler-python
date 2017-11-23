import urllib.request
import urllib.parse
import os.path
import functions
from Crawler.LinkFinder import LinkFinder
import Models.Queue.Page
import Models.Complete.Page
import Models.Queue.Link


class Page:
    def __init__(self, page_url):
        queue = Models.Queue.Page.Page
        dir(queue)
        queue.fetch()
        self.queue = queue

        complete = Models.Complete.Page.Page
        complete.fetch()
        self.complete = complete

        link = Models.Queue.Link.Link
        link.fetch()
        self.link = link

        self.page_url = page_url
        self.queue.add(page_url)
        urlres = urllib.parse.urlparse(page_url)
        self.base_url = urlres.netloc
        self.scheme = urlres.scheme
        self.links = set()

    def add(self, link):
        full_url = self.sanitize_url(link)
        if full_url:
            self.queue.add(full_url)
        return self

    def fetch_links(self):
        """
        Get all the anchor tag url from the website
        :return:
        """
        url_finder = LinkFinder(self.page_url)
        url_finder.feed(url_finder.html_string())
        self.links = url_finder.get_values()
        return self.links

    def links(self):
        return self.links

    def _merge_links(self):
        for lk in self.links:
            self.link.add(lk)
        return self.link.links

    def queued(self):
        return self.queue.links

    def completed(self):
        self.complete.links

    def save(self):
        self.queue.save()

    def save_links(self):
        self.fetch_links()
        self._merge_links()
        self.link.save()

    def get_base_url(self) -> object:
        """
        Return Base url of the page. Like www.example.com/home.php will be www.example.com
        :rtype: object
        """
        return self.base_url

    def sanitize_url(self, url):
        """
        Santitize url and return full if partial
        :param url:
        :return:
        """
        return urllib.parse.urljoin(self.scheme + "://" + self.base_url, url)
