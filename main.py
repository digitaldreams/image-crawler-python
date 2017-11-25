from Image import Save
from Models.Complete.Image import Image
import os.path;
from Crawler.Page import Page
from Crawler.Image import Image
from Image.Download import Download
import functions
import threading
from queue import Queue

if __name__ == '__main__':
    NUMBER_OF_THREADS = 4
    queue = Queue()
    page = Page('http://fdfashionbd.com')
    links = page.fetch_links()


    def create_jobs():
        for link in sorted(links):
            queue.put(link)
        queue.join()


    # Create worker threads (will die when main exits)
    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=downloading)
            t.daemon = True
            t.start()


    def downloading():
        while True:
            try:
                link = queue.get()
                print(threading.current_thread().name + ' fetching ' + link)
                img = Image(link)

                images = img.fetch_links()
                down = Download(links=images, path=functions.get_folder_name(link))
                down.start()
                queue.task_done()
                print(threading.current_thread().name + ' Done ' + link)
                if queue.empty():
                    break
            except:
                queue.task_done()
                continue




    create_workers()
    create_jobs()
