from html.parser import HTMLParser
import urllib.parse
import functions


class ImgFinder(HTMLParser):
    def __init__(self, page_url):
        urlres = urllib.parse.urlparse(page_url)
        self.page_url = page_url
        self.base_url = urlres.netloc
        self.folder = functions.get_folder_name(urlres.netloc)
        self.path = urlres.path
        self.src = set()
        HTMLParser.__init__(self)
    """
    This function called by HTMLParser internally. We modify it to make our work
    """
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for (attr, value) in attrs:
                if attr == 'src':
                    fullUrl = urllib.parse.urljoin(self.base_url, value)
                    self.src.add(fullUrl)
                else:
                    continue

    def getSrc(self):
        return self.src

    def get_base_url(self):
        return self.base_url

    def save_to_file(self):
        file_name = self.folder_path()+ self.path + '.txt'
        with open(file_name, 'w') as f:
            for line in sorted(self.src):
                f.write(line + '\n')

        return file_name

    def folder_path(self):
        return "storage/" + self.folder
