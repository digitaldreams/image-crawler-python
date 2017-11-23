from UrlFinder import UrlFinder


class ImgFinder(UrlFinder):
    def __init__(self, page_url):
        UrlFinder.__init__(self, page_url, 'img', 'src')
