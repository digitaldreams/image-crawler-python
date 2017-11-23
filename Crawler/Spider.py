import urllib.request
import urllib.parse
import os.path
import functions
from Crawler.LinkFinder import LinkFinder


class Spider:
    domain = ''

    def __init__(self, page_url):
        self.queue = set();
        self.complete = set();
        self.page_url = page_url
        urlres = urllib.parse.urlparse(page_url)
        self.base_url = urlres.netloc
        self.scheme = urlres.scheme
        self.path = urlres.path.replace("/", "_")
        self.folder = functions.get_folder_name(urlres.netloc)
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

    def queued(self):
        return self.queue

    def completed(self):
        self.complete

    def init_files(self):
        pass

    def get_base_url(self) -> object:
        """
        Return Base url of the page. Like www.example.com/home.php will be www.example.com
        :rtype: object
        """
        return self.base_url

    def save_to_file(self) -> object:
        """
        Save waiting downloadable image to queue. So next time when program run
        :rtype: object
        """
        file_name = self.folder_path() + "/" + self.path + '.txt'
        with open(file_name, 'w') as f:
            for line in sorted(self.src):
                f.write(line + '\n')

        return file_name

    def folder_path(self) -> object:
        """
         Path to folder resource where images and others file will be saved for current domain relative to current folder
        :return: object
        """
        return "storage/" + self.folder

    def sanitize_url(self, url):
        """
        Santitize url and return full if partial
        :param url:
        :return:
        """
        return urllib.parse.urljoin(self.scheme + "://" + self.base_url, url)
