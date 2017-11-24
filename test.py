from Image import Save
from Models.Complete.Image import Image
import os.path;
from Crawler.Page import Page
from Crawler.Image import Image
from Image.Download import Download

if __name__ == '__main__':
    # page=Page('https://gopostie.com')
    # page.save_links()

    # img = Image('https://gopostie.com')
    # img.save_links()

    down = Download()
    down.start()
