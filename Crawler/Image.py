import urllib.parse
from Crawler.ImgFinder import ImgFinder
import Models.Queue.Image
import Models.Queue.Link


class Image:
    def __init__(self, page_url):

        self.image = Models.Queue.Image.Image()
        self.link = Models.Queue.Link.Link()

        self.page_url = page_url
        urlres = urllib.parse.urlparse(page_url)
        self.base_url = urlres.netloc
        self.images = set()

    def add(self, link):
        full_url = self.sanitize_url(link)
        if full_url:
            self.images.add(full_url)
        return self

    def fetch_links(self):
        """
        Get all the anchor tag url from the website
        :return:
        """
        img_finder = ImgFinder(self.page_url)
        img_finder.feed(img_finder.html_string())
        self.images = img_finder.get_values()
        return self.images

    def links(self):
        return self.images

    def _merge_links(self):
        for lk in self.images:
            self.image.add(lk)
        return self.image.links

    def save(self):
        self._merge_links()
        self.image.save()

    def save_links(self):
        self.fetch_links()
        self.save()
        self.update_link()

    def update_link(self):
        self.link.remove(self.page_url)
        self.link.save()
