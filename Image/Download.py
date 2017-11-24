import errno
import os.path
import Models.Queue.Image
import Models.Complete.Image
from Image import Save


class Download():
    path = 'storage/images'

    def __init__(self, take=None):
        self.queue = Models.Queue.Image.Image()
        self.complete = Models.Complete.Image.Image()
        self.limit = take
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def start(self) -> object:
        """
        Start Downloading file
        :rtype: object
        """
        if isinstance(self.limit, int) and len(self.queue.links) >= self.limit:
            links = sorted(self.queue.links)[0:self.limit]
        else:
            links = self.queue.links

        for file in links:
            try:
                img = Save.Save(file, self.path)
                img.save()
            except Exception as e:
                print(str(e))
            self.complete.add(file)
        self.save()

    def save(self) -> object:
        """
        Update links txt file
        :return : None
        """
        self.queue.links = self.queue.links.difference(self.complete.links)
        self.queue.save()
        self.complete.save()
