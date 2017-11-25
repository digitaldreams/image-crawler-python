import os.path
import urllib.parse
import urllib.request

from Crawler import ImgFinder


def gather_img_src(page_url) -> object:
    """
    Parse Html and find img source and return as set
    :param page_url:
    :return: object
    """
    try:
        html = html_string(page_url)
        finder = ImgFinder.ImgFinder(page_url)
        finder.feed(html)
    except Exception as e:
        print(str(e))
        return set()

    return finder.getSrc()


def create_project_folder(page_url: object) -> object:
    """
    Create a project folder
    :param page_url:
    :rtype: object
    """
    base_url = get_folder_name(urllib.parse.urlparse(page_url).netloc)
    if not os.path.exists("storage/" + base_url):
        os.makedirs("storage/" + base_url)


# Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
def html_string(page_url: object) -> object:
    """
    Fetch html from url and return as Html String
    :param page_url:
    :rtype: object
    """
    html_string = ''
    try:
        request = urllib.request.Request(page_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
        response = urllib.request.urlopen(request)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")

    except Exception as e:
        print(str(e))
    return html_string


def get_folder_name(base_url) -> object:
    """
    Get hostname from a base url like www.example.com will return example
    :param base_url:
    :rtype: object
    """
    base_url=urllib.parse.urlparse(base_url).netloc
    parts = base_url.split(".")
    if len(parts) == 3:
        return parts[1]
    elif len(parts) == 2:
        return parts[0]
    else:
        return "-".join(parts)
