from Image import Save
from Models.Complete.Image import Image
import os.path;
from Crawler.Page import Page
if __name__ == '__main__':
    page=Page('https://gopostie.com')
    page.save()
    page.save_links()