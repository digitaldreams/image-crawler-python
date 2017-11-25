import errno
import os.path
import Models.Queue.Image
import Models.Complete.Image
from Image import Save


class Download():
    folder = 'storage/'

    def __init__(self, take=None, links=None, path="images"):
        self.queue = Models.Queue.Image.Image()
        self.complete = Models.Complete.Image.Image()
        self.limit = take
        self.path = self.folder + path

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        if isinstance(links, set):
            self.links = links
        else:
            self.links = self.queue.links

    def start(self) -> object:
        """
        Start Downloading file
        :rtype: object
        """
        if isinstance(self.limit, int) and len(self.links) >= self.limit:
            links = sorted(self.links)[0:self.limit]
        else:
            links = self.links

        for file in links:
            try:
                img = Save.Save(file, self.path)
                img.save()
            except Exception as e:
                print(str(e))
            self.complete.add(file)
        return self

    def save(self) -> object:
        """
        Update links txt file
        :return : None
        """
        self.queue.links = self.queue.links.difference(self.complete.links)
        self.queue.save()
        self.complete.save()
