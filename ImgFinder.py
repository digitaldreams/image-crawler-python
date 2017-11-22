from html.parser import HTMLParser
import urllib.parse
import functions


class ImgFinder(HTMLParser):
    def __init__(self, page_url):
        urlres = urllib.parse.urlparse(page_url)
        self.page_url = page_url
        self.base_url = urlres.netloc
        self.folder = functions.get_folder_name(urlres.netloc)
        self.path = urlres.path.replace("/", "_")
        self.scheme = urlres.scheme
        self.src = set()
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        """
        This function called by HTMLParser internally. We modify it to make our work

        :rtype: object
        """
        if tag == 'img':
            for (attr, value) in attrs:
                if attr == 'src':
                    fullUrl = urllib.parse.urljoin(self.scheme + "://" + self.base_url, value)
                    self.src.add(fullUrl)
                else:
                    continue

    def getSrc(self) -> object:
        """
        List of image link as set
        :return: object
        """
        return self.src

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
