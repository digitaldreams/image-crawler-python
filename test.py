from Crawler.Page import Page
from Crawler.Image import Image
from Image.Download import Download

if __name__ == '__main__':
    page = Page('http://fdfashionltd.com');
    # fetch all the links (anchor) of this website
    links = page.fetch_links();

    for link in links:
        # fetch all of the images of a web url
        img = Image(link);
        images = img.fetch_links();
        # Download all of the images
        download = Download(links=links)
        download.start()
