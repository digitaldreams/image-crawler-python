from Image import Save
from Models.Complete.Image import Image
import os.path;
from Crawler.Page import Page
from Crawler.Image import Image
from Image.Download import Download
import functions

if __name__ == '__main__':
    page = Page('https://gopostie.com')
    links = page.fetch_links()
    for link in sorted(links):
        print('Downloading ...' + link)
        img = Image(link)
        images = img.fetch_links()
        down = Download(links=images,path=functions.get_folder_name(link))
        down.start()
        # down = Download()
        # down.start()
